export default function guardfail(mathFunction) {
  const queue = [];
  try {
    queue.push(mathFunction());
  } catch (err) {
    queue.push(`${err}`);
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}
