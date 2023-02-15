import user_interface as ui
import calculations as calc
import set_sample as ss


def control_system():
    # result = calc.get_result(ss.get_data(ui.inputing()))
    # ui.user_output(result)
    user_input = ui.inputing()
    result = calc.get_result(ss.get_data(user_input))
    ui.user_output(user_input, result)