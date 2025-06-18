package com.learning.datastructures.lists;


public class SinglyLinkedList<T> {

    private Node<T> head;

    SinglyLinkedList() {
        this.head = null;
    }

    public void add(final T value) {
        Node<T> node = new Node<>(value);
        if(head == null) {
            this.head = node;
        }
        else {
            Node<T> curr =  head;
            while (curr.next != null) {
                curr = curr.next;
            }
            curr.next = node;
        }
    }

    public void traverse() {
        Node<T> curr =  head;
        while (curr.next != null) {
            System.out.print(curr.value + "->");
            curr = curr.next;
        }
        System.out.println(curr.value);
    }

    static class Node<T> {

        T value;
        Node<T> next;

        Node(T value) {
            this.value = value;
            this.next = null;
        }
    }

    public static void main(String[] args) {
        SinglyLinkedList<String> list = new SinglyLinkedList<>();

        //list.add("Hello");
        //list.add("friend");
        //list.add("nice");

        list.traverse();
    }
}