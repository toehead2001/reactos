/* This file is autogenerated. */

typedef int (*TestRoutine)(int Command, char *Buffer);

extern int Fs_1Test(int Command, char *Buffer);
extern int Mdl_1Test(int Command, char *Buffer);
extern int Mdl_2Test(int Command, char *Buffer);
extern int Mm_1Test(int Command, char *Buffer);

extern void AddTest(TestRoutine Routine);

void RegisterTests()
{
  AddTest((TestRoutine)Fs_1Test);
  AddTest((TestRoutine)Mdl_1Test);
  AddTest((TestRoutine)Mdl_2Test);
  AddTest((TestRoutine)Mm_1Test);
}
