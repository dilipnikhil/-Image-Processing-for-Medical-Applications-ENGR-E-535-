#Question 1
def bollywoodCharm(scripts, expectedCharm: int):
    #using a two pointer approach
    max_length = len(scripts)
    first = 0
    last = max_length - 1
    while first <= last:
        total = scripts[first] + scripts[last]
        if total == expectedCharm: # if they are equal in the first iteration return the indexes
            return (first, last)
        elif total > expectedCharm: # if the total is greater than expected charm
            last = last- 1 # keep moving the right pointer left
        else:
            first = first +1   # keep moving the first to the last
    return None


#Question 9
def shiftingCharacters(inputStr: str, moves: list[int]) -> str:

    alphabets = "abcdefghijklmnopqrstuvwxyz" # define a string of all the alphabets
    magic_string = ""
    
    for i in range(len(inputStr)):
        total_shift = 0 # calculate the amount of shifts for each alphabet
        for j in range(i, len(moves)):
            total_shift = total_shift + moves[j] #calculate the total shifts for every alphabets
        move_to_do = (total_shift + alphabets.index(inputStr[i])) % 26 #if it exceeds 26, get the remainder
        magic_string = magic_string + alphabets[move_to_do] # add to the magic string
    
    return magic_string

#question 3
def cheapestWarhead(valuations: list) -> int:
    #lets again use a two pointer approach
    #initialize pointers
    left = 0
    right = 1
    maxdamage = 0  # initialize max damage to zero

    while right < len(valuations): # as long as left is less than the len of the input array
        if valuations[left] <= valuations[right]:
            damage = valuations[right] - valuations[left] # calculate the damage
            if damage > maxdamage: # if the calculated damage is greater then assign max damage as damage
                maxdamage = damage
            right += 1 #move right pointer to right
        else:
            left += 1 #keep mving the left pointer left
            right = left + 1  #Reset right pointer to one more than left pointer

    return maxdamage



#QUestion 7
def maxWaterStorage(pillarsHeight: list[int]) -> int:
  
  # using two pointer approach here as well
  #initiate the pointers and area to zero
  left, right = 0 , len(pillarsHeight)-1
  max_area = 0
  while left < right:
    area = min(pillarsHeight[left],pillarsHeight[right]) * (right - left) # calculate the area, basic
    #print(left,right)
    if area > max_area:
      max_area = area
    else:
      if pillarsHeight[left] < pillarsHeight[right]:
        left = left + 1 #increment to the right
      else:
        right = right - 1 #decrement to the left
  return max_area


#Question 2
def checkIsGeneDerived(G1: str,G2: str)->bool:

    if len(G1) > len(G2):
      return False # check for first condition ie. len of small string bigger than the bigger string that should be searched in

    g1Count, g2Count = [0]*26, [0]*26 # initiate two arrays of length of 26, that can be updated with frequencies of the alphabets occurence

    for i in range(len(G1)): # iterate through the length of the G1 on both G1 and G2 and update their frequencies by calculting the ascii value of that alphabet and subtracting it with the ascii value of "a"
      g1Count[ord(G1[i]) - ord("a")] = g1Count[ord(G1[i]) - ord("a")] + 1
      g2Count[ord(G2[i]) - ord("a")] = g2Count[ord(G2[i]) - ord("a")] + 1

    if g1Count == g2Count: # compare two arrays and check 
      return True

    left = 0 # because we have already checked for the first len(G1) in G2, we move forward from that point
    for right in range(len(G1),len(G2)):
      g2Count[ord(G2[right]) - ord("a")] = g2Count[ord(G2[right]) - ord("a")] + 1 # we update the frequency
      g2Count[ord(G2[left]) - ord("a")] = g2Count[ord(G2[left]) - ord("a")] - 1 # and we delete the value of the previous alphabet
      left = left +1 # keep moving the pointer
      if g1Count == g2Count:
        print(g1Count, g2Count)
        return True
    return False


def specialString(n: int) -> int:
  magical_string = [1,2,2] # the idea here is use the starting of the magical string and generate the length "n" string
  i = 2 # initiate to 2 as that is the index of the last element in the magical string
  while len(magical_string) < n: 
      right = magical_string[-1] #get the last element in the magical string
      left = 3 - right # for the first iteration left = 1. we use three to subtract from right to get the previous number to add to the magical string
      magical_string.extend([left] * magical_string[i]) #extend the string based on left and right
      i = i + 1 # incremnt i to the next value
  return magical_string[:n].count(1)



class Node:
    def __init__ (self, val):
        self.data = val
        self.next = None

# we will do this by using tow pointer first, slow and fast
def detect_cycle(head):
    # initiate both pointers to be at head

    slow = head
    fast = head

    while fast and fast.next: # check if the node and next node is available because we are using fast.next.next
        slow = slow.next
        fast = fast.next.next # move fast
        if slow == fast:  # if both the pointers meet, voila, we have a list
            return slow #return the node
    return None

def cycle_buster(head):

    point_of_cycle = detect_cycle(head) # we get the node where the slow and fast met

    if not point_of_cycle: # if there is no cycle, the detect cycle returns None, so that will just return the head of the LL
        return head
    
    # now lets find the tail who's reference needs to be changed to none
    pointer1 = head #inititate first pointer to head
    pointer2 = point_of_cycle

    while pointer1 != pointer2: # keep moving the pointer till they reach the same reference from the node
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    while pointer2.next != pointer1: # check if pointer two is referrring to the pointer one
        pointer2 = pointer2.next # this is the point where the reference has to be removed

    pointer2.next = None  # Break the cycle

    return head  # Return the head of the modified linked list
