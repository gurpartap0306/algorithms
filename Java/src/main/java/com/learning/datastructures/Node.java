package com.learning.datastructures;

import java.util.ArrayList;
import java.util.List;

public class Node<T> {

    final T value;
    final List<Node<T>> children;

    Node(final T value) {
        this.value = value;
        this.children = new ArrayList<>();
    }

    Node(final T value, final List<Node<T>> children) {
        this.value = value;
        this.children = children;
    }

    public T getValue() {
        return value;
    }

    public void addChild(final Node<T> child) {
        children.add(child);
    }

    public List<Node<T>> getChildren() {
        return children;
    }

}