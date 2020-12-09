from datetime import datetime
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import DataLoader
import torchvision.datasets as datasets
import torchvision.transforms as transforms

class CNN(nn.Module):
    def __init__(self, input_size, num_classes):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=8, kernel_size=(3,3), stride=(1,1), padding=(1,1))

class NN(nn.Module):
    def __init__(self, input_size, num_classes):
        super(NN, self).__init__()
        self.fc1 = nn.Linear(input_size, 50)
        self.fc2 = nn.Linear(50, num_classes)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x


# Hyperparameters
input_size = 784
num_classes = 10
learning_rate = 0.001
batch_size = 32
num_epochs = 1

# Set device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load data
# This transform converts numpy arrays to tensors
transform = transforms.ToTensor()
train_dataset = datasets.MNIST(root='dataset', train=True, transform=transform, download=True)
train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_dataset = datasets.MNIST(root='dataset', train=False, transform=transform, download=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=True)

# Init network
model = NN(input_size=input_size, num_classes=num_classes).to(device)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

start_time = datetime.now()
# Train
for epoch in range(num_epochs):
    # Each epoch goes through entire train_dataset
    for batch_idx, (data, targets) in enumerate(train_loader):
        # Go through each batch in the train_dataset
        # data = images
        # targets = ground truth labels
        data = data.to(device=device)
        targets = targets.to(device=device)

        # print(data.shape) prints torch.Size([64, 1, 28, 28])
        # 64 batches, 1 color channel (grayscale), 28x28 pixels

        # Reduce 4 dimensions [64, 1, 28, 28] into two [64, 784]
        # -1 means infer the size of the second dimension
        # while keeping the same number of elements
        # https://stackoverflow.com/a/50793899
        data = data.reshape(data.shape[0], -1)

        # Forward
        scores = model(data)
        loss = criterion(scores, targets)

        # backward
        # Set all the gradients to zero for each batch
        # so that it doesn't store backprop calculations
        # from previous forward propagations
        optimizer.zero_grad()

        loss.backward()

        # gradient descent or adam step
        # Update the weights depending on the gradients computed here
        optimizer.step()
print(f'Training took: {datetime.now()-start_time}')

# Check accuracy on training and test
def check_accuracy(loader, model):
    if loader.dataset.train:
        print("Train data")
    else:
        print("Test data")
    num_correct = 0
    num_samples = 0
    model.eval()

    # Don't compute gradients (unnecessary) when checking the model
    with torch.no_grad():
        for x, y in loader:
            x = x.to(device=device)
            y = y.to(device=device)
            x = x.reshape(x.shape[0], -1)

            scores = model(x)
            _, predictions = scores.max(1)

            num_correct += (predictions == y).sum()
            num_samples += predictions.size(0)
        print(f'Got {num_correct} / {num_samples} with accuracy {float(num_correct)/float(num_samples)*100:.2f}')

    model.train()

    l = [module for module in model.modules() if type(module) != nn.Sequential]

    print(l)

check_accuracy(train_loader, model)
check_accuracy(test_loader, model)
