import json

treatment_arms = ["Drug A", "Drug B"]  # List of treatments
populations = [
        {"age": "18-45", "gender": "Male"},
        {"age": "18-45", "gender": "Female"}
    ]

result = {
            "treatment_arms": [
                {
                    "treatment_arm": treatment,
                    **population
                }
                for treatment in treatment_arms
                for population in populations
            ]
        }

print(json.dumps(result, indent=4))

# Output

# {
#     "treatment_arms": [
#         {
#             "treatment_arm": "Drug A",
#             "age": "18-45",
#             "gender": "Male"
#         },
#         {
#             "treatment_arm": "Drug A",
#             "age": "18-45",
#             "gender": "Female"
#         },
#         {
#             "treatment_arm": "Drug B",
#             "age": "18-45",
#             "gender": "Male"
#         },
#         {
#             "treatment_arm": "Drug B",
#             "age": "18-45",
#             "gender": "Female"
#         }
#     ]
# }