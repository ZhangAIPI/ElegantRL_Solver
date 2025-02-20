import torch as th
import torch
device = th.device("cuda:0")
N = 10
num_env = 100
max_dim = 2
test_state = torch.ones((num_env, N + 2, N + 2), device=device).to(torch.float32)
# The generated key value is a random value of 1 or 2
# test_state = torch.randint(0,max_dim, (num_env, N + 2, N + 2), device=device).to(torch.float32)
mask = th.zeros(N + 2, N + 2).to(device)
mask[1, 1] = 1
for i in range(2, N + 1):
    mask[i, i-1] = 1
    mask[i, i] = 1

mask = mask.reshape(-1).repeat(1, num_env).reshape(num_env, N + 2, N + 2).to(device)
test_state = th.mul(test_state, mask)
test_state += th.ones_like(test_state)
with open(f"test_data_tensor_train_N={N}.pkl", 'wb') as f:
    import pickle as pkl
    pkl.dump(test_state, f)
