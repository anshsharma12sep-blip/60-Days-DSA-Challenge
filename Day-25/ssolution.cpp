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

class Solution {
public:
    bool hasCycle(ListNode* head) {
        // Edge case: empty list or single node
        if (head == NULL || head->next == NULL) {
            return false;
        }

        ListNode* slow = head;
        ListNode* fast = head;

        while (fast != NULL && fast->next != NULL) {
            slow = slow->next;          // Move 1 step
            fast = fast->next->next;    // Move 2 steps

            if (slow == fast) {
                return true;  // Cycle detected
            }
        }

        return false;  // No cycle
    }
};

int main() {
    // Creating nodes
    ListNode* node1 = new ListNode(1);
    ListNode* node2 = new ListNode(2);
    ListNode* node3 = new ListNode(3);
    ListNode* node4 = new ListNode(4);

    // Linking nodes
    node1->next = node2;
    node2->next = node3;
    node3->next = node4;

    // Create cycle
    node4->next = node2;

    Solution obj;
    cout << obj.hasCycle(node1);  // Output: 1 (true)

    return 0;
}