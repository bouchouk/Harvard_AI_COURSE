import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        evidence_list = []
        label_list = []
        month = {'Jan':0 ,"Feb":1 ,"Mar":2,"Apr":3 ,"May":4 ,"June":5 ,"Jul":6 ,"Aug":7 ,"Sep":8 ,"Oct":9 ,"Nov":10 ,"Dec":11}
        count = 0
        for row in csv_reader:
            if count != 0:
                evidence = row[:-1]
                label = row[-1]
                evidence[10] = month[evidence[10]]
                evidence[15] = 1 if evidence[15] == "Returning_Visitor" else 0
                evidence[16] = 0 if evidence[16] == "FALSE" else 1
                label = 0 if label == "FALSE" else 1
                evidence = [float(item) for item in evidence]
                evidence_list.append(evidence)
                label_list.append(label)
            else:
                count = 1
    return evidence_list , label_list

    


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)
    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    total_True = 0
    total_True_predicted = 0
    total_False = 0
    total_False_predicted = 0
    for label , prediction in zip(labels, predictions):
        if label == 1:
            total_True += 1
            if label == prediction:
                total_True_predicted += 1
        else: 
            total_False += 1
            if label == prediction:
                total_False_predicted += 1
    if total_True != 0:
        sensitivity = total_True_predicted / total_True
    else :
        sensitivity = 1
    if total_False != 0:
        specificity = total_False_predicted / total_False
    else:
        specificity = 1
    return sensitivity ,specificity
            


if __name__ == "__main__":
    main()
