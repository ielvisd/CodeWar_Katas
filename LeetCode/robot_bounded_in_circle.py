class Solution:
    
    def isRobotBounded(self, instructions):
      self.x = 0
      self.y = 0
      self.facing = 'north'
      instructions_list = []
      
      # Helper function that will update our location/direction the
      # robot is facing when passed in an instruction
      def move(instruction):
        if instruction == "G":
          if self.facing == 'north':
            self.y += 1
          elif self.facing == 'east':
            self.x += 1
          elif self.facing == 'south':
            self.y -= 1          
          elif self.facing == 'west':
            self.x -= 1

        elif instruction == "L":
          if self.facing == 'north':
            self.facing = 'west'
          elif self.facing == 'east':
            self.facing = 'north'
          elif self.facing == 'south':
            self.facing = 'east'          
          elif self.facing == 'west':
            self.facing = 'south'

        elif instruction == "R":
          if self.facing == 'north':
            self.facing = 'east'
          elif self.facing == 'east':
            self.facing = 'south'
          elif self.facing == 'south':
            self.facing = 'west'          
          elif self.facing == 'west':
            self.facing = 'north'
      
      # Add instructions to instructions list
      for instruction in instructions:
        instructions_list.append(instruction)
      
      # If the list is empty return True    
      if len(instructions_list) == 0:
        return True
            
      # If there's Left and Right are not in the list return False
      # It will move in a straight line forever
      if 'L' not in instructions_list and 'R' not in instructions_list:
        return False
        
      # Otherwise move three times and record the new location each time
      # I can probably cut this to two times
      for instruction in instructions_list:
          move(instruction)

      location1 = [self.x, self.y]

      for instruction in instructions_list:
          move(instruction)
          
      location2 = [self.x, self.y]
        
      for instruction in instructions_list:
          move(instruction)
          
      location3 = [self.x, self.y]
            
      # If either x or y are equal between locations 1 & 2        
      if location1[0] == location2[0] or location1[1] == location2[1]:
          # If either x or y are equal between locations 1 & 3
          if location1[0] == location3[0]:
              # If the difference between x or y's at 1 & 3 is greater 
              # than 1 return false, otherwise return true
              if abs(location3[1] - location1[1]) > 1:
                  return False
              else:
                  return True
          elif location1[1] == location3[1]:
              if abs(location3[0] - location1[0]) > 1:
                  return False
              else:
                  return True
          else:      
            return True
      # If locations 1 and 3 are inverses of each other return True        
      elif location1[0] == location3[1] and -location1[1] == location3[0]:
          return True
      elif location3[0] == location1[1] and -location3[1] == location1[0]:
          return True
      # If locations 1 and 3 are the same return True      
      elif location3[0] == location1[0] and location3[1] == location1[1]:
          return True
      else:
          return False
      return
  