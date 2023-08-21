normal_sh_path=$(dirname "$(realpath "${BASH_SOURCE[0]}")")
source "$normal_sh_path/../common/autosysbench.sh"
normal_sh_path=$(dirname "$(realpath "${BASH_SOURCE[0]}")")


main() {
  test_result_path="$normal_sh_path/../data/debug"
  mkdir $test_result_path
  deleteSysbenchPods



  getPodLogs $test_result_path
  transform /Users/earayu/Documents/GitHub/sysbench-output-parser/sysparser $test_result_path

  python3 "$normal_sh_path/../plot/main.py"
}
