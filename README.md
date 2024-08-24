# git_assignment_HeroVired

# Assignment 1
Work on a Python application called "CalculatorPlus." The application provides basic arithmetic operations, such as addition, subtraction, multiplication, and division.  1st create a "dev" branch and make a basic calculator with function add, subtract, multiple and divide. Then the task is to implement a new feature that adds support for calculating the square root of a number. Add the square root function by creating a new branch called "feature/sqrt". While working on this new branch "feature/sqrt" a bug was reported wherein we have to report an error if a number is getting divided by zero. Make necessary changes in the "dev" branch while keeping feature/sqrt branch up to date. After completing the feature implementation and ensuring that the application works correctly, create a pull request targeting the main branch.

# Assignment 2 
create a branch ‘lfs’. Upload any large file whose size is over ‘200mb’ and try to push this file into the repository.
 integrate Git LFS (Large File Storage) to handle these files efficiently.
      $ git checkout -b lfs
        Switched to a new branch 'lfs'
      $ git lfs track "*.gz"
        Tracking "*.gz"
      $ git add .gitattributes
      $ git commit -m "Add Git LFS tracking for large files"
        [lfs bbc86aa] Add Git LFS tracking for large files
         1 file changed, 1 insertion(+)
         create mode 100644 .gitattributes
      $ git push origin lfs




# Assignment 3


