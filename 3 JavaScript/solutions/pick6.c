#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_ITER 100000
#define TICKET_LENGTH 6

void generateTicket(int *ticket);
int compareTickets(int *ticket1, int *ticket2);

int main() {
    int winnings = 0, expenses = 0, nIter = 0;
    float roi;
    int winningTicket[TICKET_LENGTH];
    int ticket[TICKET_LENGTH];

    srand(time(NULL));

    int prizes[] = {0, 4, 7, 100, 50000, 1000000, 25000000};

    generateTicket(winningTicket);

    while (nIter < MAX_ITER) {
        expenses += 2;
        nIter++;

        generateTicket(ticket);
        winnings += prizes[compareTickets(winningTicket, ticket)];
    }

    printf("\nwinnings: %d\nexpenses: %d\nroi: %f\n\n", winnings, expenses, (float)(winnings - expenses) / expenses);

    return 0;
}


void generateTicket(int *ticket) {
    for(int i = 0; i < TICKET_LENGTH; i++) 
        *(ticket + i) = rand() % 99 + 1;
}


int compareTickets(int *ticket1, int *ticket2) {
    int i, matches = 0;
    for (i = 0; i < TICKET_LENGTH; i++) {
        if (ticket1[i] == ticket2[i])
            matches++;
    }
    return matches;
}