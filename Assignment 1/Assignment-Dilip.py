
    


#Question 3
def cheapestWarhead(valuations:list())->int:
  left = 0
  right = 1
  maxdamage = 0
  while (right < len(valuations)) :
    if valuations[left] <= valuations[right]:
      damage = valuations[right] - valuations[left]
      if damage > maxdamage:
        maxdamage = damage
      else:
        right = right + 1
    else:
        left = left + 1
        right = right + 1
  return maxdamage

#QUestion 7
def maxWaterStorage(pillarsHeight: list[int]) -> int:
  left, right = 0 , len(pillarsHeight)-1
  max_area = 0
  while left < right:
    area = min(pillarsHeight[left],pillarsHeight[right]) * (right - left)
    #print(left,right)
    if area > max_area:
      max_area = area
    else:
      if pillarsHeight[left] < pillarsHeight[right]:
        left = left + 1
      else:
        right = right - 1
  return max_area


#Question 2
def checkIsGeneDerived(G1: str,G2: str)->bool:

    if len(G1) > len(G2):
      return False

    g1Count, g2Count = [0]*26, [0]*26

    for i in range(len(G1)):
      g1Count[ord(G1[i]) - ord("a")] = g1Count[ord(G1[i]) - ord("a")] + 1
      g2Count[ord(G2[i]) - ord("a")] = g2Count[ord(G2[i]) - ord("a")] + 1

    if g1Count == g2Count:
      return True

    left = 0
    for right in range(len(G1),len(G2)):
      g2Count[ord(G2[right]) - ord("a")] = g2Count[ord(G2[right]) - ord("a")] + 1
      g2Count[ord(G2[left]) - ord("a")] = g2Count[ord(G2[left]) - ord("a")] - 1
      left = left +1
      if g1Count == g2Count:
        print(g1Count, g2Count)
        return True
    return False

def specialString(n: int) -> int:
  magical_string = [1,2,2]
  i = 2
  while len(magical_string) < n:
      right = magical_string[-1]
      left = 3 - right
      magical_string.extend([left] * magical_string[i])
      i = i + 1
  return magical_string[:n].count(1)


class Node:
    def __init__ (self, val):
        self.data = val
        self.next = None

def detect_cycle(head):
    slow = head
    fast = head

    while fast and fast.next: # check if the node and next node is available because we are using fast.next.next
        slow = slow.next
        fast = fast.next.next

        if slow == fast:  # at this point we can say that there is a loop in the given linked List
            return slow
        
    return None

def cycle_buster(head):
    point_of_cycle = detect_cycle(head)

    if not point_of_cycle:
        return head
    
    pointer1 = head
    pointer2 = point_of_cycle

    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
        
    while pointer2.next != pointer1.next:
        pointer2 = pointer2.next

    pointer2.next = None  # Break the cycle

    return head  # Return the head of the modified linked list

            
    