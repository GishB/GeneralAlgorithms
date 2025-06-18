

for epoch in range(epochs):
    for (inputs, labels) in train_loader:
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        optimizer.step()