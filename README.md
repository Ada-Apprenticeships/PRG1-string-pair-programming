# **Pair Programming Challenge \- Username Validator & Generator**

## 🎯 Learning Objectives

- Practice string manipulation techniques  
- Apply functions, sequence, selection, and iteration  
- Work collaboratively using pair programming  
- Build a practical tool with real-world applications

## 👥 Pair Programming Roles

**Driver**: Types the code, focuses on syntax and implementation details  
**Navigator**: Reviews code, suggests approaches, catches errors, thinks strategically

**Switch roles every 15 minutes\!** Set a timer on your phone.

## 🚀 Getting Started in GitHub Codespaces

1. One of you fork this GitHub repo, and open up your fork in Codespaces.  
2. Don’t forget to commit and sync every time you make a meaningful change.

## 📋 Core Challenge: Username Validator

Create a function that checks if a username meets these basic requirements:

### Basic Requirements (Start Here\!)

A valid username must:

1. Be between 3 and 20 characters long  
2. Start with a letter  
3. Contain only letters, numbers, and underscores  
4. Not have consecutive underscores (\_\_ is invalid)

### Implementation Tasks

**Task 1: Length Check** ⭐

```py
def check_length(username):
    # Return True if username is 3-20 characters
    # Hint: use len() function
```

**Task 2: First Character Check** ⭐

```py
def check_first_char(username):
    # Return True if first character is a letter
    # Hint: username[0] gets first character
    # Hint: .isalpha() checks if character is a letter
```

**Task 3: Valid Characters Check** ⭐⭐

```py
def check_valid_chars(username):
    # Return True if all characters are letters, numbers, or underscore
    # Hint: iterate through each character
    # Hint: use .isalnum() or check against allowed characters
```

**Task 4: No Consecutive Underscores** ⭐⭐

```py
def check_no_double_underscore(username):
    # Return True if username doesn't contain "__"
    # Hint: use the 'in' operator to check for substring
```

**Task 5: Combine All Checks** ⭐⭐ Update your `check_username()` function to use all validation functions and provide specific feedback:

```py
def check_username():
    username = input("Enter username to check: ")
    
    # Check all requirements and give specific feedback
    # Example output:
    # ✓ Length is valid (8 characters)
    # ✗ Must start with a letter
    # ✓ Contains only valid characters
    # ✓ No consecutive underscores
```

## 🎨 Extension 1: Username Generator

Create a function that generates usernames based on user input:

**Basic Generator Tasks:**

1. **From Full Name** ⭐⭐  
     
   - Input: "John Smith"  
   - Possible outputs: "jsmith", "john\_s", "j\_smith"

   

2. **Add Random Numbers** ⭐⭐

```py
import random
# Add 2-4 random digits to the end
# Example: "jsmith" → "jsmith742"
```

3. **Handle Spaces and Special Characters** ⭐⭐⭐  
     
   - Remove or replace invalid characters  
   - "John O'Brien" → "john\_obrien"

## 🚀 Extension 2: Advanced Features

Choose one or more to implement:

### A. Username Scoring System ⭐⭐⭐

Rate usernames on creativity and security:

```py
def score_username(username):
    score = 0
    # +10 points for optimal length (8-15 chars)
    # +5 points for mix of letters and numbers
    # +5 points for underscore usage
    # -5 points for common patterns (e.g., "user123", "test")
    # Return score out of 100
```

### B. Swearing Filter ⭐⭐⭐

```py
def contains_inappropriate(username):
    banned_words = ["spam", "fake", "test"]  # Add more
    # Check if username contains any banned words
    # Be clever - check for l33t speak too! (e.g., "sp4m")
```

### C. Username Suggestions ⭐⭐⭐⭐

When a username is taken or invalid, suggest alternatives:

```py
def suggest_alternatives(username):
    suggestions = []
    # Add numbers: username + random 3 digits
    # Add year: username + "2024"
    # Add underscores: split and rejoin with _
    # Reverse parts: "johnsmith" → "smithjohn"
    return suggestions
```

### D. Case Style Converter ⭐⭐⭐⭐

```py
def convert_case_style(username, style):
    # style can be: "lower", "upper", "camel", "snake"
    # Examples:
    # "JohnSmith" + "snake" → "john_smith"
    # "john_smith" + "camel" → "johnSmith"
```

## 🎮 Extension 3: Interactive Menu System

Enhance the main menu with these features:

1. **Batch Check** \- Check multiple usernames at once  
2. **Save History** \- Remember checked/generated usernames  
3. **Statistics** \- Show most common validation failures  
4. **Custom Rules** \- Let users define their own validation rules

## 💡 Tips for Success

### String Methods to Explore:

- `.lower()`, `.upper()` \- Change case  
- `.strip()` \- Remove whitespace  
- `.replace(old, new)` \- Replace characters  
- `.startswith()`, `.endswith()` \- Check beginning/end  
- `.find()` \- Find substring position  
- `.count()` \- Count occurrences

### Debugging Tips:

1. Print intermediate values to see what's happening  
2. Test with edge cases: "", "a", "ab", very long strings  
3. Test with special characters and numbers  
4. Use descriptive variable names

## 🏁 Checkpoint Questions

After completing the core challenge, you should be able to answer:

1. How do you access individual characters in a string?  
2. What's the difference between .isalpha() and .isalnum()?  
3. How can you check if a substring exists within a string?  
4. Why might iterating through a string be useful?

## 📝 Submission Checklist

Before you finish:

- [ ] Core validation functions work correctly  
- [ ] Program provides clear user feedback  
- [ ] Both partners have driven for equal time  
- [ ] At least one extension attempted  
- [ ] Edge cases tested (empty string, single character, etc.)

**Remember:** The goal is to learn and practice, not to rush through. Take time to understand each concept and help your partner when they're stuck\!  