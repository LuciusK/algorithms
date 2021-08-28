import torch
'''
IOU算法
'''
def iou(box1:torch.Tensor(), box2:torch.Tensor()) -> torch.Tensor():
    # 假设box1维度为[N,4]   box2维度为[M,4]
    N = box1.size(0)
    M = box2.size(0)
    upleft = torch.max(
        box1[:, :2].unsqueeze(1).expand(N, M, 2), # [N, 2]->[N, 1, 2]->[N, M, 2]
        box2[:, :2].unsqueeze(0).expand(N, M, 2), # [M, 2]->[1, M, 2]->[N, M, 2]
    )
    downright = torch.min(
        box1[:, 2:].unsqueeze(1).expand(N, M, 2), 
        box2[:, 2:].unsqueeze(0).expand(N, M, 2),
    )
    wh = downright - upleft + 1 # [N, M, 2]
    wh[wh < 0] = 0 # 不重叠皆为0
    inter = wh[:, :, 0] * wh[:, :, 1] # [N, M]

    area1 = (box1[:, 2] - box1[:, 0] + 1) * (box1[:, 3] - box1[:, 1] + 1) # [N, ]
    area2 = (box2[:, 2] - box2[:, 0] + 1) * (box2[:, 3] - box2[:, 1] + 1) # [M, ]
    area1 = area1.unsqueeze(1).expand(N, M) # [N, M]
    area2 = area2.unsqueeze(0).expand(N, M) # [N, M]

    iou = inter / (area1 + area2 - inter)
    return iou

'''
NMS算法一般是为了去掉模型预测后的多余框，其一般设有一个nms_threshold=0.5，具体的实现思路如下：

1. 选取这类box中scores最大的哪一个，记为box_best，并保留它
2. 计算box_best与其余的box的IOU
3. 如果其IOU>0.5了，那么就舍弃这个box（由于可能这两个box表示同一目标，所以保留分数高的哪一个）
4. 从最后剩余的boxes中，再找出最大scores的哪一个，如此循环往复
'''

def nms(bboxes:torch.Tensor(), scores:torch.Tensor(), threshold:int) -> torch.LongTensor():
    '''
    bboxes维度为[N, 4]，scores维度为[N, ], 均为tensor
    '''
    x1 = bboxes[:, 0]
    y1 = bboxes[:, 1]
    x2 = bboxes[:, 2]
    y2 = bboxes[:, 3]
    areas = (x2 - x1 + 1) * (y2 - y1 + 1) # [N, ] 每个bbox的面积
    _, rank = scores.sort(0, descending=True) # 降序排列

    keep = []
    while rank.numel() > 0: # torch.numel()返回张量元素个数
        i = rank[0].item() # 保留scores最大的那个框box[i]
        keep.append(i)
        if rank.numel() == 1: # 保留框只剩一个
            break
        # 计算box[i]与其余各框的IOU
        xx1 = x1[rank[1:]].clamp(min=x1[i]) # [N-1, ]
        yy1 = y1[rank[1:]].clamp(min=y1[i])
        xx2 = x2[rank[1:]].clamp(max=x2[i])
        yy2 = y2[rank[1:]].clamp(max=y2[i])
        inter = (xx2 - xx1 + 1).clamp(min=0) * (yy2 - yy1 + 1).clamp(min=0) # [N-1, ]

        iou = inter / (areas[i] + areas[rank[1:]] - inter)
        idx = (iou <= threshold).nonzero().squeeze() # 此时idx为[N-1, ] 而order为[N, ], nonzero()返回的是二维张量
        if idx.numel() == 0:
            break
        rank = rank[idx + 1]
    return torch.LongTensor(keep)