data={
  "policyId": "POL-983472",
  "policyType": "Health Insurance",
  "customer": {
    "customerId": "CUS-67381",
    "name": "Arun Kumar",
    "age": 42,
    "address": {
      "street": "14 MG Road",
      "city": "Bengaluru",
      "pincode": "560001",
      "state": "Karnataka"
    },
    "contact": {
      "email": "arun.kumar@example.com",
      "phone": "+91-98450-12345"
    }
  },
  "coverage": {
    "sumInsured": 500000,
    "startDate": "2024-05-10",
    "endDate": "2025-05-09",
    "inclusions": [
      "Hospitalization",
      "Pre & Post Hospitalization",
      "Diagnostics",
      "Ambulance Cover"
    ],
    "exclusions": ["Cosmetic Procedures", "Non-prescribed Treatments"]
  },
  "claims": [
    {
      "claimId": "CLM-82931",
      "dateOfClaim": "2024-09-12",
      "hospital": "Apollo Hospital",
      "claimAmount": 48000,
      "approvedAmount": 45000,
      "diagnosis": "Kidney Stone",
      "status": "Approved"
    },
    {
      "claimId": "CLM-83910",
      "dateOfClaim": "2024-12-02",
      "hospital": "Fortis Healthcare",
      "claimAmount": 125000,
      "approvedAmount": 0,
      "diagnosis": "Knee Surgery",
      "status": "Rejected",
      "rejectionReason": "Under waiting period"
    }
  ],
  "premium": {
    "annualPremium": 22500,
    "tax": 4050,
    "totalPayable": 26550,
    "paymentHistory": [
      {
        "paymentId": "PAY-8821",
        "date": "2024-05-10",
        "amount": 26550,
        "mode": "Credit Card",
        "status": "Success"
      }
    ]
  }
}


# Write a function that takes the above JSON and returns the total approved amount across all claims.

# print(data["claims"][1]["approvedAmount"])
# print(len(data["claims"]))

def total_approved():

  total_approved_amount = 0
  for i in range(int(len(data["claims"]))):
    total_approved_amount = total_approved_amount + data["claims"][i]["approvedAmount"]
  

  return total_approved_amount


run = total_approved()
print(run)


# Write a function to extract all claims where status is Rejected AND claimAmount > 50000, returning them as a list of dictionaries
 



# approvedAmount