import pandas as pd

def csvFileSplitter(fileName, numFiles):
    '''
    Creator: bjornm
    Purpose: Simple .csv file splitter to break up a csv file into a number of files by even row count.
    '''
    
    file = pd.read_csv(fileName) 
    numLines = len(file)
    colHeaders = list( file.columns)
    rowSize = round(len(file) / numFiles)

    for batchRows in range(0, numLines, rowSize):
        df =  pd.read_csv(fileName, nrows = rowSize , skiprows = batchRows)
        df.columns = colHeaders 
        output_csv = fileName + '-' + str(batchRows) + '.csv'
        df.to_csv(output_csv, index=False, header=True, mode='a', chunksize = rowSize)

    if __name__ == '__main__':
        fileName = input("Enter the name of the .csv file that you would like to split up into N files: ")
        numFiles = input("Enter the number of the files you would like the split to result in?: ")
        csvFileSplitter(fileName, numFiles) # run function
