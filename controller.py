import user_interface as ui
import calculations as calc
import set_sample as ss
import logger as log


def control_system():
    # result = calc.get_result(ss.get_data(ui.inputing()))
    # ui.user_output(result)
    user_input = ui.inputing()
    log.add_log(f'User typed {user_input}')
    result = calc.get_result(ss.get_data(user_input))
    ui.user_output(user_input, result)