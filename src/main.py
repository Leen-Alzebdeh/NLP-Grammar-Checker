import sys
import nltk
import csv


def main():

    # first is a path to the input data file
    # the second is a path to the grammar file
    # third is a path to the output TSV file
    if len(sys.argv) == 4:
        input_path = sys.argv[1]
        gram_path = sys.argv[2]
        output_path = sys.argv[3]
    else:
        input_path = "data/train.tsv"
        gram_path = "grammars/toy.cfg"
        output_path = "output/train.tsv"

    const_parse(input_path, gram_path, output_path)


def const_parse(input_path, gram_path, output_path):
    '''
    parse the constituents, determine if grammar for each doc is correct or not, and calculate precision, recall and confusion mtx values
    Input:
        input_path (str): path to input train tsv file
        gram_path (str): path to grammar you built
        output_path (str): path where you want to output predictions
    return None
    '''
    TP, TN, FP, FN = 0, 0, 0, 0
    cfg = nltk.data.load(gram_path)
    parser = nltk.ChartParser(cfg)  # not sure about this

    with open(input_path, newline='') as csvfile, open(output_path, 'w', newline='') as output_file:
        csvreader = csv.reader(csvfile, delimiter='\t')
        csvwriter = csv.writer(output_file, delimiter='\t')

        # write header
        csvwriter.writerow(["id", "ground_truth", "prediction"])

        # skip header
        next(csvreader)

        # parse each sentence
        for row in csvreader:
            if len(row) == 1:
                continue
            sentence_id, label, pos = row[0], row[1], row[-1].split()

            try:
                if list(parser.parse(pos)):
                    prediction = "0"  # correct grammar
                else:
                    prediction = "1"  # incorrect grammar
            except:
                prediction = "3"  # error

            csvwriter.writerow([sentence_id, label, prediction])
            TP, TN, FP, FN = evaluate(
                label, prediction, sentence_id, pos, TP, TN, FP, FN)

    # Precision = TP / (TP + FP)
    # Recall = TP / (TP + FN)
    print("Precision is {}".format(TP/(TP+FP)))
    print("Recall is {}".format(TP/(TP+FN)))
    print("Values of TP, TN, FP, FN: {}, {}, {}, {}".format(TP, TN, FP, FN))


def evaluate(label, prediction, TP, TN, FP, FN):
    '''
    calculate confusion mtx values given a doc and current confusion mtx
    input
        label: actual label for doc (0 if correct, 1 otherwise)
        prediction (int): predicted label
        TP (int): true positives
        TN (int): true negatives
        FP (int): false positive
        FN (int): false negative
    return 
        TP (int): true positives
        TN (int): true negatives
        FP (int): false positive
        FN (int): false negative

    '''
    if label == prediction:
        if int(label):
            return TP+1, TN, FP, FN
        else:
            return TP, TN+1, FP, FN
    else:
        if int(label):
            return TP, TN, FP, FN+1
        else:
            return TP, TN, FP+1, FN


if __name__ == "__main__":
    main()
