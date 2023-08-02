const accordion = document.querySelector('.accordion');
const currButton = document.querySelector('.currTrigger');
const nextButton = document.querySelector('.nextTrigger');
const contentCurrent = document.querySelector('.panel-current');
const contentNext = document.querySelector('.panel-next');
const panelCurr = document.querySelector('.current-emp');
const panelNext = document.querySelector('.next-emp');



accordion.addEventListener('click', (e) => {
    const activePanel = e.target.closest(".accordion-panel");
    if (!activePanel) return;
    if (activePanel.id == 'curr-emp') {
        currButton.setAttribute('aria-expanded', "true");
        nextButton.setAttribute('aria-expanded', "false");
        contentCurrent.setAttribute('aria-hidden', "false");
        contentNext.setAttribute('aria-hidden', "true");
        panelCurr.setAttribute('curr-data-active', "true");
        panelNext.setAttribute('next-data-active', "false");
    }
    else {
        currButton.setAttribute('aria-expanded', "false");
        nextButton.setAttribute('aria-expanded', "true");
        contentCurrent.setAttribute('aria-hidden', "true");
        contentNext.setAttribute('aria-hidden', "false");
        panelCurr.setAttribute('curr-data-active', "false");
        panelNext.setAttribute('next-data-active', "true");
    }
});