import torch #파이토치

'''t = torch.tensor([0., 1., 2., 3., 4., 5., 6.])
print(t.dim())
print(t.shape)
print(t.size())'''

t = torch.FloatTensor([[1., 2., 3.],
                       [4., 5., 6.],
                       [7., 8., 9.],
                       [10., 11., 12.]
                      ])
print(t)
