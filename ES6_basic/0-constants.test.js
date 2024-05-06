import { taskFirst, getLast, taskNext } from './0-constants';

describe('0-constants', () => {
  test('taskFirst returns correct string', () => {
    expect(taskFirst()).toBe('I prefer const when I can.');
  });

  test('getLast returns correct string', () => {
    expect(getLast()).toBe(' is okay');
  });

  test('taskNext returns correct string', () => {
    expect(taskNext()).toBe('But sometimes let is okay');
  });
});