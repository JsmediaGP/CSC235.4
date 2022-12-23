import matplotlib.pyplot as plt


def compare(a: list, b: list) -> bool:
    # This function return boolean and it compares two lists of elements
    list_length = len(a)
    for i in range(list_length):
        if a[i] != b[i]:
            return False
    return True


def global_terrorist() -> dict:
    # Opening of the text file and passing it to a variable
    txtfile = open('terror.txt', 'r')
    terrorist_lines = txtfile.readlines()
    txtfile.close()
    # Get the total feature of terrorist from the first line {index 0}
    total_terror_f = int(terrorist_lines[0])
    # Create serial number for the  feature (starting from 1)
    s_no = list(range(1, total_terror_f + 1))
    # Create a list that will hold the feature later on
    terrorist = [0] * total_terror_f
    # Create a list that will hold the sum of the feature later on
    terror_sum = [0] * total_terror_f
    # list for the id of similar feature later on
    similarity_id = [0] * total_terror_f
    # Get all features and sum of the features
    for counter in range(1, total_terror_f + 1):
        # This line will get all features into the terrorist multidimentional list
        # Making sure to clean all newline identifiers and split them so that they can be easy dealt with later
        terrorist[counter - 1] = terrorist_lines[counter].strip('\n').split(',')
        # This line will sum up the feature and add it to its corresponding index
        terror_sum[counter - 1] = sum([int(i) for i in terrorist[counter - 1]])
    # This block will check similarity between features and put in their currensponding similarity id respectively
    for i in range(total_terror_f):
        for j in range(total_terror_f):
            if (i == j): continue  # This is to make sure that the program is not checking similarity against itself
            # If features has the same sum it might be possible they have the same features
            if (terror_sum[i] == terror_sum[j]):
                # This line will check if the two features is the same
                # Similar to terrorist[i] == terrorist[j] which is like explicit way of doing it.
                same_terror = compare(terrorist[i], terrorist[j])
                # This line check if the features are similar, it should add the serial number(id) of the similar feature for the current feature
                if same_terror: similarity_id[i] = j + 1

    # The program return the serial number, feature, sum and the similarity id
    return {
        's_no': s_no,
        'feature': terrorist,
        'sum': terror_sum,
        'duplicate': similarity_id
    }


def table_row(*iterables):
    # This is a helper function that print out iterables like a table row
    for i in iterables:
        print(str(i).ljust(20), end='')
    print()


def to_table(data: dict) -> None:
    # function to print the data response from the global terrorist program
    print('GLOBAL TERRORIST')
    table_row('s_no', 'Feature', 'SUM', 'Duplicate')
    total = len(
        data['s_no'])  # Get the total features from the length of serial number.This can be get many ways though.
    for i in range(total):
        s_no = data['s_no'][i]
        feature = ','.join(data['feature'][i])
        feature_sum = data['sum'][i]
        duplicate = data['duplicate'][i]
        table_row(s_no, feature, feature_sum, duplicate)


def graph_show(data: dict) -> None:
    # This function display the data response from global terrorist program in a bar chart
    y = data['duplicate']
    x = data['s_no']
    plt.bar(x, y, label='duplicate serial number')
    plt.bar(x, y, color='green')
    plt.title("A graph of Duplicate Values and Serial number")
    plt.xlabel('Serial Number')
    plt.ylabel('Duplicate')

    plt.legend()
    plt.show()


def occurence_table(data: dict) -> None:
    feature = data['feature']
    occurence = {','.join(i): 0 for i in feature}
    for i in feature:
        lookup = ','.join(i)
        count = occurence.get(lookup)
        occurence[lookup] = count + 1
    table_row('s_no', 'Feature', 'Occurence')
    feature_set = list(occurence.keys())
    cases = range(1, len(feature_set) + 1)
    for s_no in cases:
        current_feature = feature_set[s_no - 1]
        current_occurence = occurence[current_feature]
        table_row(s_no, current_feature, current_occurence)


def occurence_graph(data: dict) -> None:
    # This function display the occurence of features in data response from global terrorist program in a bar chart
    feature = data['feature']
    occurence = {','.join(i): 0 for i in
                 feature}  # Initializing an hash table for the occurence with default value of zero(0)
    # Increment the occurence of the features by 1 per occurence
    for i in feature:
        lookup = ','.join(i)
        count = occurence.get(lookup)
        occurence[lookup] = count + 1

    x = range(1, len(occurence.keys()) + 1)  # X hold the features
    y = occurence.values()  # Y hold the occurence value
    plt.title('Graph of occurence of features')
    plt.xlabel('Features')
    plt.ylabel('Occurence')
    plt.bar(x, y)
    plt.bar(x, y, color='blue')
    plt.show()


# driver code
if __name__ == '__main__':
    data = global_terrorist()
    to_table(data)
    print('\n\n')
    occurence_table(data)
    occurence_graph(data)

