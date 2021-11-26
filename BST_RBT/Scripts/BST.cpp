#include <bits/stdc++.h>
#include <iostream>
#include <ctime>
#include <sys/time.h>
#include <iostream>
#include <string> 
#include <fstream>
#include <sstream>

using namespace std;

int heightofTree = 0;

struct Node {
    int key;
    Node* l;
    Node* r;
    Node* p;
    Node(int x): key(x), l(nullptr), r(nullptr), p(nullptr) {}
};

struct Tree {
    Node* root;
    Tree() : root(nullptr) {}
};

void tree_insert(Tree &T, Node* z)
{
    Node* y = nullptr;
    Node* x  = T.root;
    while(x != nullptr) {
        y = x;
        if(z->key < x->key){
            x = x->l;
        }
        else{
            x = x->r;
        }
    }
    z -> p = y;
    if(y == nullptr){
        T.root = z;
    }
    else if(z->key < y->key){
        y->l = z;
    }
    else{
        y->r = z;
    }
}

Node* minimum(Node* x){
    while(x->l != nullptr){
        x = x->l;
    }
    return x;
}


Node* treeSearch(Node* x, int k){
    if(x == nullptr || k == x->key){
        return x;
    }
    if(k < x->key){
        return treeSearch(x->l, k);
    }
    return treeSearch(x->r, k);
}

void transplant(Tree &T, Node* u, Node* v)
{
    if(u->p == nullptr){
        T.root = v;
    } 
    else if(u == u->p->l){
        u->p->l = v;
    }
    else{
        u->p->r = v;
    }
    if(v != nullptr){
        v->p = u->p;
    }
}

void tree_delete(Tree &T, Node* z)
{
    if(z->l == nullptr){
        transplant(T, z, z->r);
    }
    else if(z->r == nullptr){
        transplant(T, z, z->l);
    }
    else{
        Node* y = minimum(z->r);
        if(y->p != z){
            transplant(T, y, y->r);
            y->r = z->r;
            y->r->p = y;
        }
        transplant(T, z, y);
        y->l = z->l;
        y->l->p = y;
    }
}

void inorderTreeWalk(Node* x){
    if(x != nullptr){
        inorderTreeWalk(x->l);
        cout << x->key << " ";
        inorderTreeWalk(x->r);
    }
}


int height(Node * node)  // return the height of tree
	{
		if(node == NULL)
			return -1;    
		else
		{	
            int left=height(node->l);   
            int right=height(node->r); 
             if (left > right)          
                 return left+1; 
             else
                return right+1;
		}
	}

double run_experiment(int n, int arrayNums[],double* d_time)
{
    Tree T;
    struct timeval beginB, endB, beginD, endD;
    
    for (int i = 0; i < n; i++)
    {
        arrayNums[i] = rand() % 100 + 1;
    }
    gettimeofday(&beginB, 0);
    for (int i = 0 ; i < n;i++){
        tree_insert(T, new Node(arrayNums[i]));
    }
    gettimeofday(&endB, 0);
    long seconds = endB.tv_sec - beginB.tv_sec;
    long microseconds = endB.tv_usec - beginB.tv_usec;
    double elapsed = seconds + microseconds*1e-6;
    printf("Time measured: %.3f seconds.\n", elapsed);
    heightofTree = height(T.root);
    cout << "\nHeight of tree is " << heightofTree;
    cout << "\n" << endl;
    gettimeofday(&beginD, 0);
    for (int i = 0 ; i < n; i++){
        Node* tmp = treeSearch(T.root, arrayNums[i]);
        tree_delete(T, tmp);
    }
    gettimeofday(&endD, 0);
    long secondsD = endD.tv_sec - beginD.tv_sec;
    long microsecondsD = endD.tv_usec - beginD.tv_usec;
    *d_time = secondsD + microsecondsD*1e-6;
    inorderTreeWalk(T.root);
    return elapsed;
}

int main()
{
    int nums[9] = {10000, 25000, 50000, 100000, 250000,350000,500000,750000, 1000000};
    double times[9];
    double dtimes[9];
    double d_time;
    int* arrayNums;
    arrayNums = new int[1000000];
    double times_build[9];
    fstream file;
    file.open("data.csv");
    file << "n,time,dtime,avgH" << "\n";
    for (int i = 0; i < 9; i++)
    {
        times_build[i] = run_experiment(nums[i], arrayNums, &d_time);
        file << nums[i] << "," << times_build[i] << "," << d_time << "," << heightofTree << "\n";
        heightofTree = 0;
    }


    file.close();
    
    return 0;
}