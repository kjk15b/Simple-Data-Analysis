#include "Riostream.h"

void basic() {
	TString dir = gSystem->UnixPathName(__FILE__);
	dir.ReplaceAll("basic.C", "");
	dir.ReplaceALL("/./", "/");

	ifstream in;
	in.open(Form("%sbasic.dat", dir.Data()));
}
