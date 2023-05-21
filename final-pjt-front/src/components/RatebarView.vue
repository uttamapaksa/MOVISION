<template>
<div id="ratebar">
  <form class="range" action="">
    <label class="range__label" for="dummy">Range</label>
    <input class="range__input" id="dummy" type="range" value="5" min="0" max="10" step="1">
    <div class="range__output" aria-hidden="true" data-tip>
      <div class="range__output-value-track">
        <div class="range__output-values" data-values></div>
      </div>
    </div>
  </form>
</div>
</template>

<script>
export default {
  name: 'RatebarView',
  mounted() {
    window.addEventListener("DOMContentLoaded",() => {
      const fr = new RangeSlidingValue("dummy");
      console.log(fr)
    });

    class RangeSlidingValue {
      constructor(id) {
        this.input = document.getElementById(id);
        this.output = document.querySelector('[data-tip]');
        this.values = this.output?.querySelector("[data-values]");
        this.init();
      }
      init() {
        this.input?.addEventListener("input",this.update.bind(this));
        this.populateValues();
        this.update();
      }
      populateValues() {
        const digitSpan = document.createElement("span");
        digitSpan.className = "range__output-value";

        const { min, max } = this.input;

        for (let v = min; v <= max; ++v) {
          const newSpan = digitSpan.cloneNode();
          newSpan.innerText = v;
          this.values?.appendChild(newSpan);
        }
      }
      update(e) {
        let value = this.input.defaultValue;
        // when manually set
        if (e) value = e.target?.value;
        // when initiated
        else this.input.value = value;

        const min = this.input.min || 0;
        const max = this.input.max || 100;
        const possibleValues = max - min;
        const relativeValue = (value - min) / possibleValues;
        const percentRaw = relativeValue * 100;
        const percent = +percentRaw.toFixed(2);
        const tipWidth = 2;
        const transXRaw = -tipWidth * relativeValue * possibleValues;
        const transX = +transXRaw.toFixed(2);
        const prop1 = "--percent";
        const prop2 = "--transX";

        this.input?.style.setProperty(prop1,`${percent}%`);
        this.output?.style.setProperty(prop1,`${percent}%`);
        this.values?.style.setProperty(prop2,`${transX}em`);
      }
    }
  },
}
</script>

<style>
#ratebar {
  --hue: 223;
  --white: hsl(0,0%,100%);
  --lt-gray: hsl(var(--hue),10%,95%);
  --primary0: hsl(var(--hue),90%,95%);
  --primary1: hsl(var(--hue),90%,90%);
  --primary3: hsl(var(--hue),90%,50%);
  --primary4: hsl(var(--hue),90%,30%);
  /* --primary5: hsl(var(--hue),90%,10%); */
  --trans-dur: 0.3s;
  font-size: calc(16px + (32 - 16) * (100vw - 320px) / (1280 - 320));
}
#ratebar > body,
#ratebar > input {
  font: 1em/1.5 "DM Sans", sans-serif;
}
#ratebar > body {
  background-color: var(--primary0);
  color: var(--primary5);
  height: 100vh;
  display: grid;
  place-items: center;
  transition:
    background-color var(--trans-dur),
    color var(--trans-dur);
}

/* Main styles */
.range {
  margin: 2.5em 0.75em 0 0.75em;
  padding-top: 0.5em;
  position: relative;
  max-width: 12em;
  width: 100%;
}
.range__label {
  overflow: hidden;
  position: relative;
  width: 1px;
  height: 1px;
}
.range__input {
  --percent: 50%;
  background-color: var(--primary1);
  background-image: linear-gradient(var(--primary3),var(--primary3));
  background-size: var(--percent) 100%;
  background-repeat: no-repeat;
  border-radius: 0.25em;
  display: block;
  margin: 0.5em -0.75em;
  width: calc(100% + 1.5em);
  height: 0.5em;
  transition: background-color var(--trans-dur);
  -webkit-appearance: none;
  appearance: none;
  -webkit-tap-highlight-color: transparent;
}
.range__input:focus {
  outline: transparent;
}

/* WebKit */
.range__input::-webkit-slider-thumb {
  background-color: var(--white);
  border: 0;
  border-radius: 50%;
  box-shadow: 0 0.125em 0.5em hsl(0,0%,0%,0.3);
  width: 1.5em;
  height: 1.5em;
  transition: background-color 0.15s linear;
  -webkit-appearance: none;
  appearance: none;
}
.range__input:focus::-webkit-slider-thumb,
.range__input::-webkit-slider-thumb:hover {
  background-color: var(--lt-gray);
}

/* Firefox */
.range__input::-moz-range-thumb {
  background-color: var(--white);
  border: 0;
  border-radius: 50%;
  box-shadow: 0 0.125em 0.5em hsl(0,0%,0%,0.3);
  width: 1.5em;
  height: 1.5em;
  transition: background-color 0.15s linear;
}
.range__input:focus::-moz-range-thumb,
.range__input::-moz-range-thumb:hover {
  background-color: var(--lt-gray);
}

/* Continue main styles */
.range__output,
.range__output:after,
.range__output-value-track,
.range__output-values {
  position: absolute;
}
.range__output,
.range__output:after {
  transform: translateX(-50%);
}
.range__output {
  --percent: 50%;
  background-color: var(--primary3);
  border-radius: 0.25em;
  color: var(--white);
  padding: 0.25em;
  bottom: calc(100% + 0.5em);
  left: var(--percent);
  text-align: center;
  width: 2em;
  height: 2em;
  transition: background-color var(--trans-dur);
}
.range__output:after {
  border-top: 0.5em solid var(--primary3);
  border-left: 0.5em solid transparent;
  border-right: 0.5em solid transparent;
  content: "";
  display: block;
  top: calc(100% - 1px);
  left: 50%;
  width: 0;
  height: 0;
}
.range__output-value-track {
  inset: 0;
  overflow: hidden;
}
.range__output-values {
  --transX: 0;
  display: flex;
  align-items: center;
  white-space: nowrap;
  top: 0;
  left: 0;
  height: 100%;
  transform: translateX(var(--transX));
  transition: transform 0.15s linear;
}
.range__output-value {
  width: 2em;
}

/* `:focus-visible` support */
@supports selector(:focus-visible) {
  .range__input:focus::-webkit-slider-thumb {
    background-color: var(--white);
  }
  .range__input:focus-visible::-webkit-slider-thumb,
  .range__input::-webkit-slider-thumb:hover {
    background-color: var(--lt-gray);
  }
  .range__input:focus::-moz-range-thumb {
    background-color: var(--white);
  }
  .range__input:focus-visible::-moz-range-thumb,
  .range__input::-moz-range-thumb:hover {
    background-color: var(--lt-gray);
  }
}

/* Dark theme */
@media (prefers-color-scheme: dark) {
  body {
    background-color: var(--primary5);
    color: var(--primary1);
  }
  .range__input {
    background-color: var(--primary4);
  }
}
</style>