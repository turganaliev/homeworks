def first_last6(nums):
  return (nums[0] == 6 or nums[-1] == 6)


def common_end(a, b):
  return (a[0] == b[0] or a[-1] == b[-1])


def reverse3(nums):
  return ([nums[-1], nums[-2], nums[-3]])


def middle_way(a, b):
  return ([a[1], b[1]])


def same_first_last(nums):
  if len(nums) >= 1:
    if nums[0] == nums[-1]:
      return True
    else:
      return False
  if len(nums) == 0:
    return False


def sum3(nums):
  return (nums[0] + nums[1] + nums[2])


def max_end3(nums):
    return ([max(nums[0], nums[-1]),
             max(nums[0], nums[-1]),
             max(nums[0], nums[-1]),
             ])


def make_ends(nums):
  return ([nums[0], nums[-1]])


def make_pi():
  return ([3, 1, 4])


def rotate_left3(nums):
  return ([nums[1], nums[2], nums[0]])


def sum2(nums):
  if len(nums) >= 2:
    return (nums[0] + nums[1])
  if len(nums) == 1:
    return nums[0]
  else:
    return 0


def has23(nums):
  if 2 in nums or 3 in nums:
    return True
  else:
    return False

