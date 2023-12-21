<template>
  <header>
    <nav>
      <ul>
        <li><NuxtLink to="/index">About</NuxtLink></li>
        <li><NuxtLink to="/posts/1">Post 1</NuxtLink></li>
        <li><NuxtLink to="/posts/2">Post 2</NuxtLink></li>
      </ul>
    </nav>
  </header>
  <div>
    <h1>Welcome to the homepage</h1>
    <AppAlert>
      This is an auto-imported component.
    </AppAlert>
  </div>
  <img src="/public/favicon.ico" alt="Discover Nuxt 3" />
  <style>
  h1 {
    font-family: 'FarAwayGalaxy', sans-serif;
  }
  </style>

</template>