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


def evaluate(label, prediction, sentence_id, pos, TP, TN, FP, FN):
    '''
    return values: TP, TN, FP, FN
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
            print(sentence_id, prediction)
            print(pos)
            return TP, TN, FP+1, FN


if __name__ == "__main__":
    main()
