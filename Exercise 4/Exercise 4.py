import csv

def load_dataset(file_path):
    dataset = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        for row in csv_reader:
            dataset.append(row)
    return headers, dataset

def calculate_priors(dataset, outcome_index):
    outcome_counts = {}
    total_count = len(dataset)

    for row in dataset:
        outcome = row[outcome_index]
        if outcome not in outcome_counts:
            outcome_counts[outcome] = 0
        outcome_counts[outcome] += 1

    priors = {outcome: count / total_count for outcome, count in outcome_counts.items()}
    return priors

def estimate_conditional_probs(dataset, feature_index, outcome_index):
    feature_outcome_counts = {}
    outcome_counts = {}

    for row in dataset:
        feature = row[feature_index]
        outcome = row[outcome_index]

        if outcome not in outcome_counts:
            outcome_counts[outcome] = 0
        outcome_counts[outcome] += 1

        if feature not in feature_outcome_counts:
            feature_outcome_counts[feature] = {}
        if outcome not in feature_outcome_counts[feature]:
            feature_outcome_counts[feature][outcome] = 0
        feature_outcome_counts[feature][outcome] += 1

    conditional_probs = {}
    for feature, outcomes in feature_outcome_counts.items():
        conditional_probs[feature] = {}
        for outcome, count in outcomes.items():
            conditional_probs[feature][outcome] = count / outcome_counts[outcome]

    return conditional_probs


# 4. Perform inference using Bayes' theorem
def predict_diabetes(priors, conditional_probs, evidence):
    # Calculate P(evidence | Outcome=1) and P(evidence | Outcome=0)
    p_evidence_given_diabetes = 1
    p_evidence_given_no_diabetes = 1

    for feature, value in evidence.items():
        if feature in conditional_probs:
            p_evidence_given_diabetes *= conditional_probs[feature].get(value, {}).get('1', 0)
            p_evidence_given_no_diabetes *= conditional_probs[feature].get(value, {}).get('0', 0)

    # Priors
    p_diabetes = priors.get('1', 0)
    p_no_diabetes = priors.get('0', 0)

    # Total probability of evidence
    p_evidence = (p_evidence_given_diabetes * p_diabetes) + (p_evidence_given_no_diabetes * p_no_diabetes)

    # Posterior probability P(Outcome=1 | evidence)
    p_diabetes_given_evidence = (p_evidence_given_diabetes * p_diabetes) / p_evidence if p_evidence != 0 else 0

    return p_diabetes_given_evidence

file_path = 'diabetes_dataset.csv'

headers, dataset = load_dataset(file_path)

outcome_index = headers.index('Outcome')
feature_indices = {feature: headers.index(feature) for feature in headers if feature != 'Outcome'}

priors = calculate_priors(dataset, outcome_index)

conditional_probs = {}
for feature, index in feature_indices.items():
    conditional_probs[feature] = estimate_conditional_probs(dataset, index, outcome_index)

def get_user_input():
    evidence = {}
    for feature in feature_indices:
        value = input(f"Enter the value for {feature}: ")
        evidence[feature] = value
    return evidence

user_evidence = get_user_input()

p_diabetes_given_evidence = predict_diabetes(priors, conditional_probs, user_evidence)
print(f'Probability of diabetes given evidence: {p_diabetes_given_evidence:.4f}')
