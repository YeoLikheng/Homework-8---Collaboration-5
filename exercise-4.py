def chunking_by(numbers, chunck):
    ...
    chunked_list = []
    for i in range(0, len(numbers), chunck):
        chunked_list.append(numbers[i:i+chunck])

    return chunked_list