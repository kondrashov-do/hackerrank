import java.util.*;
import java.io.*;
class Node{
    Node left,right;
    int data;
    Node(int data){
        this.data=data;
        left=right=null;
    }
}
class Solution{
  static LinkedList<Node> queue = new LinkedList<Node>();
static void levelOrder(Node t){
      if(t != null) {
        // enqueue current root
        queue.add(t);
        // while there are nodes to process
        while( !queue.isEmpty() ) {
            // dequeue next node
            Node tree = queue.pollFirst();
            //process tree's root;
            System.out.print(tree.data+ " ");
            // enqueue child elements from next level in order
            if( tree.left != null ) {
                queue.add( tree.left );
            }
            if( tree.right != null ) {
                queue.add( tree.right );
            }
        }
    }
    }
public static Node insert(Node root,int data){
        if(root==null){
            return new Node(data);
        }
        else{
            Node cur;
            if(data<=root.data){
                cur=insert(root.left,data);
                root.left=cur;
            }
            else{
                cur=insert(root.right,data);
                root.right=cur;
            }
            return root;
        }
    }
    public static void main(String args[]){
            Scanner sc=new Scanner(System.in);
            int T=sc.nextInt();
            Node root=null;
            while(T-->0){
                int data=sc.nextInt();
                root=insert(root,data);
            }
            levelOrder(root);
        }
}
