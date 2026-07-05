from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import pickle

from db import get_connection
from blockchain import store_on_blockchain

app = Flask(__name__)
CORS(app)

print("🚀 Flask started")

# Load ML Model
model = pickle.load(open('../ml/model.pkl', 'rb'))


@app.route('/')
def home():
    return "TrustChain API Running ✅"


# =========================
# Get User Details
# =========================
@app.route('/get_user', methods=['POST'])
def get_user():
    data = request.json
    aadhaar = data['aadhaar']

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM beneficiaries WHERE aadhaar=%s",
        (aadhaar,)
    )

    user = cursor.fetchone()

    conn.close()

    if not user:
        return jsonify({
            "error": "Invalid Aadhaar ❌"
        })

    return jsonify(user)


# =========================
# Apply for Scheme
# =========================
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json

        aadhaar = data['aadhaar']
        scheme_name = data['scheme']

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        # ----------------------
        # Verify Aadhaar
        # ----------------------
        cursor.execute(
            "SELECT * FROM beneficiaries WHERE aadhaar=%s",
            (aadhaar,)
        )

        user = cursor.fetchone()

        if not user:
            conn.close()
            return jsonify({
                "result": "Invalid Aadhaar ❌"
            })

        # ----------------------
        # Get Scheme Details
        # ----------------------
        cursor.execute(
            "SELECT * FROM schemes WHERE scheme_name=%s",
            (scheme_name,)
        )

        scheme = cursor.fetchone()

        if not scheme:
            conn.close()
            return jsonify({
                "result": "Invalid Scheme ❌"
            })

        income = user['income']

        # ----------------------
        # Scheme-wise Claim Count
        # ----------------------
        cursor.execute(
            """
            SELECT COUNT(*) AS count
            FROM transactions
            WHERE aadhaar=%s
            AND scheme_name=%s
            """,
            (aadhaar, scheme_name)
        )

        claim_count = cursor.fetchone()['count']

        amount = scheme['amount']

        # ======================
        # ML Fraud Detection
        # ======================
        features = pd.DataFrame(
            [[income, claim_count]],
            columns=['income', 'claim_count']
        )

        prediction = model.predict(features)[0]

        if prediction == -1:
            conn.close()

            return jsonify({
                "result": "Fraud 🚨",
                "reason": "Suspicious claim behavior detected"
            })

        # ======================
        # Eligibility Rules
        # ======================

        # Income Check
        if income > scheme['max_income']:
            conn.close()

            return jsonify({
                "result": "Not Eligible ❌",
                "reason": "Income exceeds scheme limit"
            })

        # Claim Limit Check
        if claim_count >= scheme['max_claims']:
            conn.close()

            return jsonify({
                "result": "Not Eligible ❌",
                "reason": "Claim limit exceeded"
            })

        # ======================
        # Blockchain Transaction
        # ======================
        try:
            tx_hash = store_on_blockchain(
                aadhaar,
                amount
            )

        except Exception as e:
            print("Blockchain Error:", e)
            tx_hash = "Blockchain unavailable"

        # ======================
        # Save Transaction
        # ======================
        cursor.execute(
            """
            INSERT INTO transactions
            (aadhaar, scheme_name, amount, tx_hash, status)
            VALUES (%s,%s,%s,%s,%s)
            """,
            (
                aadhaar,
                scheme_name,
                amount,
                tx_hash,
                "Approved"
            )
        )

        conn.commit()
        conn.close()

        return jsonify({
            "result": "Approved ✅",
            "amount": amount,
            "tx_hash": tx_hash,
            "claim_count": claim_count + 1
        })

    except Exception as e:
        print("Error:", e)

        return jsonify({
            "result": "Server Error ❌",
            "reason": str(e)
        })


# =========================
# Track Transaction
# =========================
@app.route('/track', methods=['POST'])
def track():

    data = request.json
    tx_hash = data.get('tx_hash')

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM transactions
        WHERE tx_hash=%s
        """,
        (tx_hash,)
    )

    record = cursor.fetchone()

    conn.close()

    if not record:
        return jsonify({
            "result": "Transaction not found ❌"
        })

    return jsonify({
        "aadhaar": record['aadhaar'],
        "scheme": record['scheme_name'],
        "amount": record['amount'],
        "status": record['status'],
        "time": str(record['created_at'])
    })


if __name__ == '__main__':
    app.run(debug=True)