import { mount } from '@vue/test-utils'
import App from './../src/App.vue'
import Calculator from './../src/components/Calculator.vue'

describe('Mounted App', () => {
  const wrapper = mount(App);
  
  it('is a Vue instance', () => {
    expect(wrapper.isVueInstance()).toBeTruthy()
  })

  it('has a button', () => {
    expect(wrapper.contains('md-button')).toBe(true)
  })

  it('renders the correct markup', () => {
    expect(wrapper.html()).toContain('y = 1x + 0')
  })

  it('responds to data changes', async () => {
    var calculator = wrapper.findComponent(Calculator)
    calculator.setData({form: {
      slope: 5,
      yIntercept: 3}
    })
    wrapper.find('md-button').trigger('click')
    await wrapper.vm.$nextTick()
    expect(wrapper.text()).toContain('y = 5x + 3')
  })
})

