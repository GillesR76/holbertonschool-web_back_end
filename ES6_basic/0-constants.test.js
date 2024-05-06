import { taskFirst, getLast, taskNext } from './0-constants';

describe('0-constants', () => {
  it('taskFirst returns correct string', () => {
    expect.assertions(1);
    expect(taskFirst()).toBe('I prefer const when I can.');
  });

  it('getLast returns correct string', () => {
    expect.assertions(1);
    expect(getLast()).toBe(' is okay');
  });

  it('taskNext returns correct string', () => {
    expect.assertions(1);
    expect(taskNext()).toBe('But sometimes let is okay');
  });
});
