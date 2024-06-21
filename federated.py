import torch
from flamby.utils import evaluate_model_on_tests
from flamby.datasets.fed_tcga_brca import (
    BATCH_SIZE,
    LR,
    NUM_EPOCHS_POOLED,
    Baseline,
    BaselineLoss,
    metric,
    NUM_CLIENTS,
    get_nb_max_rounds
)
from flamby.datasets.fed_tcga_brca import FedTcgaBrca
from flamby.strategies.fed_opt import FedAdam as strat

# Training
# Create the training data loaders
train_dataloaders = [
            torch.utils.data.DataLoader(
                FedTcgaBrca(center = 0),
                batch_size = BATCH_SIZE,
                shuffle = True,
                num_workers = 0
            ),
            torch.utils.data.DataLoader(
                FedTcgaBrca(center = 1),
                batch_size = BATCH_SIZE,
                shuffle = True,
                num_workers = 0
            )
        ]

lossfunc = BaselineLoss()
m = Baseline()
args = {
            "training_dataloaders": train_dataloaders,
            "model": m,
            "loss": lossfunc,
            "optimizer_class": torch.optim.SGD,
            "learning_rate": LR / 10.0,
            "num_updates": 100,
            "nrounds": get_nb_max_rounds(100),
        }
s = strat(**args)
m = s.run()[0]

# Testing
# Create the testing data loaders
test_dataloaders = [
            torch.utils.data.DataLoader(
                FedTcgaBrca(center = 0, train = False),
                batch_size = BATCH_SIZE,
                shuffle = False,
                num_workers = 0,
            )
        ]

dict_cindex = evaluate_model_on_tests(m, test_dataloaders, metric)

for key in dict_cindex:
    center = key.split("_")[-1]
    print("Center {}: {}".format(center, dict_cindex[key]))