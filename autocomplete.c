#include <stdio.h>

#include <string.h>

#include <stdlib.h>

#include <ctype.h>

#include "autocomplete.h"


int
rank_lexographic(void * first, void * second) {
  struct term * f = first;
  struct term * s = second;
  return strcmp(((  f) -> term), ((  s) -> term));

}
void

read_in_terms(struct term ** terms, int * pnterms, char * filename) {

  char line[200];

  char * text;

  FILE * fp = fopen(filename, "r");

  char numterms[200];

  fgets(numterms, sizeof(numterms), fp);

  * pnterms = atoi(numterms);
  struct term * array[ * pnterms];
    *terms = (struct term*) (malloc (*pnterms * sizeof(struct term)));
  for (int i = 0; i < * pnterms; i++) {

    fgets(line, sizeof(line), fp);

    char * newLine = line;

    while (isspace( * newLine)) {

      newLine++;

    }

    (*terms+i)-> weight = strtod(newLine, & text);

    while (isspace( * text)) {

      text++;

    }
    char * ending = text + strlen(text) - 1;
    while(ending > text && isspace((char)*ending)) ending--;
    ending[1]='\0';

    strcpy((*terms+i) -> term, text);

  }

  qsort(*terms, * pnterms, sizeof(struct term), rank_lexographic);

}

int

is_start(char * string, char * substr) {

  if (strlen(substr) > strlen(string))
    return 0;

  for (int i = 0; i < strlen(substr); i++) {

    if (substr[i] != string[i]) {

      return 0;

    }

  }

  return 1;

}

int
lowest_match(struct term * terms, int nterms, char * substr) {

  int first = 0;

  int last = nterms - 1;
  while (first <= last) {

    int middle = (first + last) / 2;

    char * mid = (terms + middle) -> term;

    if (is_start(mid, substr)) {

      while (is_start((terms + middle) -> term,substr) & is_start((terms+middle-1)-> term,substr)) {
        middle -= 1;

      }
      return middle;

    } else if (strcmp(substr, mid) > 0) {
      first = middle + 1;

    } else {
      last = middle - 1;
    }
  }

  return -1;

}

int

highest_match(struct term * terms, int nterms, char * substr) {

  int first = 0;

  int last = nterms-1;
  while (first <= last) {

    int middle = (first + last) / 2;

    char * mid = (terms + middle) -> term;

    if (is_start(mid, substr)) {

      while (is_start((terms + middle) -> term,substr) & is_start((terms+middle+1)-> term,substr)) {
        middle += 1;
      }
      return middle;

    } else if (strcmp(substr, mid) > 0) {
      first = middle + 1;

    } else {
      last = middle - 1;
    }
  }

  return -1;

}


int
rank_weight(const void * first,
  const void * second) {

  return   ((struct term * ) second) -> weight - ((struct term * ) first) -> weight;

}

void

autocomplete(struct term ** answer, int * n_answer, struct term * terms,
  int nterms, char * substr) {

  int first = lowest_match(terms, nterms, substr);

  int last = highest_match(terms, nterms, substr);

  if(last == -1 || first == -1){
	  * n_answer =  0;
  }else{
  * n_answer = (last - first) + 1;
  }
  * answer = (struct term * ) malloc( * n_answer * sizeof(struct term));

  for(int i = 0 ; i < *n_answer ; i ++){
      strcpy((*answer+i)->term , (terms+i+first)->term);
      (*answer+i)->weight = (terms+i+first)->weight;

  }

  qsort( * answer, * n_answer, sizeof(struct term), rank_weight);

}
