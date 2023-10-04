export default function guardfail(mathFunction) {
  const queue = [];
  try {
    queue.append(mathFunction());
  } catch (err) {
    queue.append(`${err}`);
  } finally {
    queue.append('Guardrail was processed');
  }
  return queue;
}
