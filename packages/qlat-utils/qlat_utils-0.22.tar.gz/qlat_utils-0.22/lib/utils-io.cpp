#include <qlat-utils/lib/utils-io.h>
#include <qlat-utils/qar-cache.h>

namespace qlat
{  //

void flush() { fflush(get_output_file()); }

}  // namespace qlat
