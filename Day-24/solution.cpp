#include <iostream>
using namespace std;

class ListNode {
public:
    int val;
    ListNode* next;

    ListNode(int x) {
        val = x;
        next = NULL;
    }
};

ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    // Dummy node to simplify logic
    ListNode* dummy = new ListNode(-1);
    ListNode* tail = dummy;

    while (l1 != NULL && l2 != NULL) {
        if (l1->val <= l2->val) {
            tail->next = l1;
            l1 = l1->next;
        } else {
            tail->next = l2;
            l2 = l2->next;
        }
        tail = tail->next;
    }

    // Attach remaining nodes
    if (l1 != NULL)
        tail->next = l1;
    else
        tail->next = l2;

    return dummy->next;
}

// Helper function to insert at end
ListNode* insertAtEnd(ListNode* head, int value) {
    ListNode* newNode = new ListNode(value);

    if (head == NULL)
        return newNode;

    ListNode* temp = head;
    while (temp->next != NULL)
        temp = temp->next;

    temp->next = newNode;
    return head;
}

// Helper function to print list
void printList(ListNode* head) {
    while (head != NULL) {
        cout << head->val << " -> ";
        head = head->next;
    }
    cout << "NULL" << endl;
}

// ===== MAIN FUNCTION =====
int main() {
    ListNode* list1 = NULL;
    ListNode* list2 = NULL;

    // Creating first sorted list: 1 -> 2 -> 4
    list1 = insertAtEnd(list1, 1);
    list1 = insertAtEnd(list1, 2);
    list1 = insertAtEnd(list1, 4);

    // Creating second sorted list: 1 -> 3 -> 4
    list2 = insertAtEnd(list2, 1);
    list2 = insertAtEnd(list2, 3);
    list2 = insertAtEnd(list2, 4);

    cout << "List 1: ";
    printList(list1);

    cout << "List 2: ";
    printList(list2);

    ListNode* merged = mergeTwoLists(list1, list2);

    cout << "Merged List: ";
    printList(merged);

    return 0;
}