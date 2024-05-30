export default function guardrail(mathFunction) {
  // Create an array to act as the queue
  const queue = [];

  try {
    // Execute the mathFunction and append its result to the queue
    const result = mathFunction();
    queue.push(result);

    // Append the standard message to the queue
    queue.push('Guardrail was processed');
  } catch (error) {
    // If an error is thrown, append the error message to the queue
    queue.push(`Error: ${error.message}`);

    // Append the standard message to the queue
    queue.push('Guardrail was processed');
  }

  return queue;
}
