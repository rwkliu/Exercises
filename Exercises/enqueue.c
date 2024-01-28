/*
  You are tasked with implementing a linked list to manage a queue of tasks in a system. 
  Each task is described by an ID and a priority level. 
  Your goal is to design and implement functions to manipulate this linked list.
  Design a C structure named Task to represent a task with attributes: taskID (integer) and priority (integer).
  Design a C structure named Node to represent a node in the linked list, where each node contains a Task and a pointer to the next node.
  Implement a C function enqueue that adds a new task to the end of the linked list.
  Implement a C function dequeue that removes and returns the task with the highest priority from the linked list.
  Ensure proper memory management to avoid memory leaks.
*/

#include <stdio.h>
#include <stdlib.h>

typedef struct Task {
  int taskID;
  int priority;
}  task_t;

typedef struct Node {
  task_t *task;
  struct Node *next;
}  node_t;

void print_queue(node_t *queue) {
  node_t *node_ptr = queue;

  printf("print_queue starting\n");
  while (node_ptr) {
    printf("%d\n", node_ptr->task->taskID);
    node_ptr = node_ptr->next;
  }
}

void free_queue(node_t *queue) {
  node_t *node_ptr = queue;
  node_t *next_node = queue->next;

  while (node_ptr) {
    free(node_ptr->task);
    free(node_ptr);
    node_ptr = next_node;
  }
}

node_t *enqueue(node_t *queue, int taskID, int priority) {
  node_t *node_ptr = queue;
  node_t *new_node = malloc(sizeof(node_t));
  task_t *new_task = malloc(sizeof(task_t));
  new_task->taskID = taskID;
  new_task->priority = priority;
  new_node->task = new_task;
  new_node->next = NULL;

  if (queue == NULL) {
    return new_node;
  }
  
  while (node_ptr->next) {
    node_ptr = node_ptr->next;
  }

  node_ptr->next = new_node;

  return queue;
}


task_t dequeue(node_t **queue)
{
  task_t node_task = {-1, -1};
  if (*queue == NULL) {
    return node_task;
  }
  node_t *node_to_delete = *queue;
  *queue = (*queue)->next;
  node_task.taskID = node_to_delete->task->taskID;
  node_task.priority =  node_to_delete->task->priority;
  free(node_to_delete->task);
  free(node_to_delete);
  return node_task;
}

int main() {
  printf("main starting\n");
  
  struct Node *taskQueue = NULL;

  // Enqueue tasks with different priorities
  taskQueue = enqueue(taskQueue, 1, 3);
  taskQueue = enqueue(taskQueue, 2, 1);
  taskQueue = enqueue(taskQueue, 3, 5);
  taskQueue = enqueue(taskQueue, 4, 2);

  print_queue(taskQueue);

  while (taskQueue != NULL) {
    struct Task dequeuedTask = dequeue(&taskQueue);
    if (dequeuedTask.taskID != -1) {
      printf("Dequeued Task: ID %d, Priority %d\n", dequeuedTask.taskID,
             dequeuedTask.priority);
    } else {
      printf("Queue is empty.\n");
    }
  }

  return 0;
}
