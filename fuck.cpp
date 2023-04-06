#include <iostream>
using namespace std;

int my_length(char *ptr)
{
  int counter = 0;
  int itr = 0;
  for (char *i = ptr; *(i + itr) != '\0'; itr++)
  {
    counter++;
  }
  return counter;
}

char *my_substr(int s, int l, char *ptr)
{
  if (l + s > my_length(ptr))
  {
    cout << "Invalid submission";
    char *hello = new char;
    *hello = '\0';
    return hello;
  }
  char *substr = new char;
  for (int i = 0; i < my_length(ptr); i++)
  {
    if (i == s)
    {
      for (int counter = 0; counter < l; counter++)
      {
        *(substr + counter) = *(ptr + counter + i);
      }
      break;
    }
  }
  return substr;
}

int main()
{
  cout << "Enter a string: ";
  char *str = new char;
  cin >> str;
  char *ptr = (str + 0);
  cout << "Length of entered string is: " << my_length(ptr) << endl;

  cout << "Enter the index of the starting index where you want to take your "
          "string from: ";
  int starting_point;
  cin >> starting_point;

  cout << "Enter the number of characters you want to take: ";
  int number_of_characters;
  cin >> number_of_characters;
  char *sz = my_substr(starting_point, number_of_characters, ptr);
  if (my_length(sz) != 0)
  {
    cout << "Substring is: " << sz;
  }
  else
  {
    exit(0);
  }
}