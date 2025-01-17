# How to use the widget in a Vue application
- Place the ZtWidget.vue file either in the 'src' or 'src/components' folder in your Vue project.
- Open the 'App.vue' in your project.
- Import the component at the top of the 'script' section:

```js

import ZtWidget from './components/ZtWidget.vue';

//or (based on where you placed it in the project files)

import ZtWidget from './ZtWidget.vue';

```

- Pass a 'data' prop to the widget when using it. The 'prop' should contain zero-trust-score data from a json object. example:

```html

<template>
    <ZtWidget :data="data_from_json_object" />
</template>

```

# Demonstration of the widget
- A screenshot of the widget is included in sample.jpg.
- You can include the 'sample_data.json' in your project to test the widget.
- Below is a link to an online demonstration:

https://play.vuetifyjs.com/#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