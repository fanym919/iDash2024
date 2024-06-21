# iDash Federated Learning Competition

This tool is built on FLamby. For detailed documentation and information, please visit [FLamby GitHub page](https://github.com/owkin/FLamby)

## Table of Contents
- [Dataset Description](#description)
- [Using the Dataset](#dataset)
- [Run Federated Learning](#federated)
- [Task](#task)

## Dataset Description

Preprocessed data is stored in this repo in the file ```flamby/datasets/fed_tcga_brca/brca.csv```, so the dataset does not need to be downloaded. These data are collect from 6 medical centers (0-5), and they are randomly splited into training group and testing group. Here is the number of dataset in each center.

|                      | Center 0 | Center 1 | Center 2 | Center 3 | Center 4 | Center 5 |
|----------------------|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:
| No. of Training Data | 279 | 165 | 174 | 131 | 131 | 20
| No. of Testing Data  | 32  | 31  | 32  | 31  | 31  | 31
| Total Number of Data | 311 | 196 | 206 | 162 | 162 | 51

The data for all 6 centers is presented in this format, and each data has 42 columns. You can view the raw data at ```flamby/datasets/fed_tcga_brca/brca.csv```

|                    | Dataset description
|--------------------| -----------------------------------------------------------------------------------------------
| Description        | Clinical data from the TCGA-BRCA study with 1,088 patients.
| Dataset size       | 117,5 KB (stored in this repository).
| Centers            | 6 regions - Northeast, South, West, Midwest, Europe, Canada.
| Records per center | Train/Test: 248/63, 156/40, 164/42, 129/33, 129/33, 40/11.
| Inputs shape       | 39 features (tabular data).
| Targets shape      | (E,T). E: relative risk, continuous variable. T: event observed (1) or censorship (0)
| Total nb of points | 1088.
| Task               | Survival analysis.


## Using the Dataset
Now that the dataset is ready for use you can load it using the low or high-level API
by doing:
```python
from flamby.datasets.fed_tcga_brca import FedTcgaBrca

# To load the first center as a pytorch dataset
center0 = FedTcgaBrca(center=0)
# To load the second center as a pytorch dataset
center1 = FedTcgaBrca(center=1)
```

You can execute the ```getdata.py``` file to load the data in a specific data center. Run
```
python3 getdata.py
```

## Run Federated Learning
We provide a sample program to train and test the dataset in a specific center using Federated Learning Adam. The sample script is ```federated.py```, and you can run the program with
```
python3 federated.py
```

This program includes both training and testing sections, providing an end-to-end demonstration of how to run federated learning with this tool.

The script defines the train data loader in variable ```train_dataloaders```. ```train_dataloaders``` is a ```list``` with ```torch.utils.data.DataLoader```. You can change the data center by modify ```center=0```. Meanwhile, you can train multiple center at the same time by adding extra ```torch.utils.data.DataLoader``` with different center number into ```train_dataloaders```. The valid number for data center are 0-5.

The script also define the test data loader in variable ```test_dataloaders```. ```test_dataloaders``` has the same structure as ```train_dataloaders```.

## Task
You need to develop a new federated learning algorithm for this competition. There is no need to modify any part of the tool or data reading process, as everything has already been set up and is ready to use.

The demonstration federated learning algorithm is defined in the ```solution``` function within the ```todo.py``` file. You need to rewrite this function with your algorithm. Then, you can test your algorithm with
```
python3 federated.py
```