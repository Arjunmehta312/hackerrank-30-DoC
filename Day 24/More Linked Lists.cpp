#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Node {
    public:
        int data;
        Node* next;
        Node(int d) {
            data = d;
            next = NULL;
        }
};

class Solution {
    public:
        Node* insert(Node* head, int data) {
            if (head == NULL) {
                return new Node(data);
            } else {
                Node* current = head;
                while (current->next != NULL) {
                    current = current->next;
                }
                current->next = new Node(data);
                return head;
            }
        }

        Node* removeDuplicates(Node* head) {
            if (head == NULL) return head;

            Node* current = head;
            while (current->next != NULL) {
                if (current->data == current->next->data) {
                    Node* temp = current->next;
                    current->next = current->next->next;
                    delete temp;
                } else {
                    current = current->next;
                }
            }
            return head;
        }

        void display(Node* head) {
            Node* current = head;
            while (current != NULL) {
                cout << current->data << " ";
                current = current->next;
            }
        }
};

int main() {
    Solution mylist;
    Node* head = NULL;
    int T, data;
    cin >> T;
    while (T-- > 0) {
        cin >> data;
        head = mylist.insert(head, data);
    }
    head = mylist.removeDuplicates(head);
    mylist.display(head);
    return 0;
}
