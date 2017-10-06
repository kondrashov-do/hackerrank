import java.io.*;
import java.util.*;

class Node {
	int data;
	Node next;
	Node(int d) {
        data = d;
        next = null;
    }
}

class Solution {
  public static  Node insert(Node head,int data) {
        //Complete this method
        if (head != null) {
            if (head.next != null) {
                insert(head.next, data);
            }
            else {
                head.next = new Node(data);
            }
            return head;
        }
        else {
            return new Node(data);
        }
    }

    public static void display(Node head) {
        Node start = head;
        while(start != null) {
            System.out.print(start.data + " ");
            start = start.next;
        }
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        Node head = null;
        int N = sc.nextInt();

        while(N-- > 0) {
            int ele = sc.nextInt();
            head = insert(head,ele);
        }
        display(head);
        sc.close();
    }
}
