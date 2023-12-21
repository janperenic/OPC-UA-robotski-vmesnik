<template>
    <div>
      <h1>Welcome to the homepage</h1>
      <AppAlert>
        This is an auto-imported component
      </AppAlert>
    </div>
</template>

<script>
// Use a static import for server-side compatibility
import '~/assets/css/first.css'

// Caution: Dynamic imports are not server-side compatible
import('~/assets/css/first.css')
</script>

<style>
@import url("~/assets/css/second.css");
</style>