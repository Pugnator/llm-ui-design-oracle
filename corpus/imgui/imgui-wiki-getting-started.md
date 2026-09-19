<!-- source: https://github.com/ocornut/imgui/wiki/Getting-Started
     fetched: 2026-09-19
     licence: MIT — https://github.com/ocornut/imgui/blob/master/LICENSE.txt
     title: Dear ImGui wiki — Getting Started
     version: Dear ImGui 1.93.0 WIP (master, 2026-09-19) -->

_(had to turn off wiki editing, see [Home](Home) for details. you may post meaningful wiki diff in issues/pr)_

## Index

- [Feedback Wanted!](#feedback-wanted)
- [Preamble](#preamble)
- [What is a Game Loop?](#what-is-a-game-loop)
- [Checking Out](#checking-out)
- [Compiling/Linking](#compilinglinking)
- [Setting up Dear ImGui & Backends](#setting-up-dear-imgui--backends)
- [Example: If you are using Raw Win32 API + DirectX11](#example-if-you-are-using-raw-win32-api--directx11)
- [Example: If you are using Raw Win32 API + DirectX12](#example-if-you-are-using-raw-win32-api--directx12)
- [Example: If you are using GLFW + OpenGL/WebGL](#example-if-you-are-using-glfw--openglwebgl)
- [Example: If you are using GLFW + Metal (on Apple devices)](#example-if-you-are-using-glfw--metal-on-apple-devices)
- [Example: If you are using SDL2/SDL3 + OpenGL/WebGL](#example-if-you-are-using-sdl2sdl3--openglwebgl)
- [Example: If you are using SDL2/SDL3 + Vulkan](#example-if-you-are-using-sdl2sdl3--vulkan)
- [Example: If you are using SDL3 + SDL_GPU](#example-if-you-are-using-sdl3--sdl_gpu)
- [Using another combination of backends?](#using-another-combination-of-backends)
- [Additional code to enable Docking](#additional-code-to-enable-docking)
- [Additional code to enable Multi-viewports](#additional-code-to-enable-multi-viewports)
- [Once you are setup...](#once-you-are-setup)

## Feedback Wanted!

> [!IMPORTANT] 
> After you are done setting up Dear ImGui in your application/project, please share _any feedback_ you may have in [#9040](https://github.com/ocornut/imgui/discussions/9040).<BR>Even if you made mistakes or created yourself a problem of your own, or misread a documentation: your feedback helps tweaking documentation for future users.

## Preamble 

**This is a Tutorial for getting Dear ImGui integrated in your C++ application using our standard backends.**
<BR>This is _not_ a Tutorial for _using_ the Dear ImGui API. For that, refer to the [Once you are setup...](#once-you-are-setup) section of this page.
<BR>This is _not_ a Tutorial for _implementing your own backend_. For that, refer to the [docs/BACKENDS.md](https://github.com/ocornut/imgui/blob/master/docs/BACKENDS.md) file.

**If you are using a third-party backend (e.g. Godot, raylib, Sokol, Unity, Unreal Engine, etc. see [List of third-party backends](https://github.com/ocornut/imgui/wiki/Bindings#frameworkengine-backends)):** instructions will differ, but well designed backends should either (1) mimick the naming convention of our backends either (2) provide examples or instructions.

Also refer to our [FAQ](https://github.com/ocornut/imgui/blob/master/docs/FAQ.md) and others [Wiki](https://github.com/ocornut/imgui/wiki) pages.

Before anything, **Build and run one of the examples application, play around with it.** 
<BR>With Visual Studio, open `examples/imgui_examples.sln`. XCode projects and Makefiles are also often provided.
<BR>You may not have all of the corresponding SDKs installed as we support many systems, but you should get some working out of the box.

The [examples/](https://github.com/ocornut/imgui/tree/master/examples) folder is populated with applications demonstrating Dear ImGui with a variety of common windowing and graphics API. They are designed to be as straightforward possible. However in most cases, a majority of the example-specific code is related to setting up the windowing and graphics API (aka setting up a basic application) rather than setting up Dear ImGui itself. 

If you have issues integrating Dear ImGui in your app, most of the time to easiest thing to do it refer to those [examples](https://github.com/ocornut/imgui/tree/master/examples).

For various reasons, our examples are very raw: we don't load fancy fonts and generally the Demo window cannot read anything from the filesystem, so our examples cannot showcase the use of e.g. texture.

## What is a Game Loop?

If you are already working in games you may not need to read this.

Dear ImGui comes from a game development background, where applications are expected to update continuously at interactive framerates (e.g. 60 FPS) and where it is expected that an underlying graphics-heavy application is running and showing behind Dear ImGui. This is how our examples are generally structured. While it is technically possible to lift some of those assumptions when using Dear ImGui (e.g. going idle, using variable frame rates, having no "main viewport"), those uses cases are technically possible but currently not well supported by default, requires a more intimate understanding of both the system and dear imgui, and are outside the scope of this article.

A typical game-like application taking advantage of GPU rendering would run in a loop:
```cpp
while (application_not_closed)
{
   // Poll events
   // Update application/game state
   // Render contents into a framebuffer
   // Swap/Present framebuffer to the screen
   // Wait some time (e.g. 1/60 of a second)
}
```
In the case of your example application, we explicitly attempt to synchronize to screen refresh on swap/present, making the application refresh at the natural screen refresh rate. A full-fledged application may use different timing mechanism to throttle framerate, but this is outside of our scope.

## Checking Out

It is preferable that you build yourself from sources.

- (1) Decide which branch to pull:
   - `master` or `docking`, the later adds support for [Docking](https://github.com/ocornut/imgui/wiki/Docking) and [Multi-viewports](https://github.com/ocornut/imgui/wiki/Multi-Viewports). 
   - Both branches are maintained, you can easily switch anytime.
- (2) Pull the repository into a sub-module of your project, or simply download/copy the repository in yours and commit it.

## Compiling/Linking

Dear ImGui does not mandate a particular build system. It is designed to be added to your existing application with an existing build system.

- (1) Add `imgui/` and `imgui/backends/` folders to include paths.
  - e.g. `-Irelative/path/to/imgui` with Clang/GCC.
- (2) Add files to your project or build system of your choice, so they get compiled and linked into your app.
  - Add core: all source files from the root folder: `imgui/*.cpp` and `imgui/*.h`.
  - Add backends: add `imgui/backends/imgui_impl_xxxx.cpp`/`.h` files corresponding to the technology you use from the `imgui/backends/` folder (e.g. if your app uses SDL2 + DirectX11, add `imgui_impl_sdl2.cpp`/`.h` and `imgui_impl_dx11.cpp`/`.h` etc.). If your engine uses multiple APIs you may include multiple backends.
  - Misc: Debugger users: See [misc/debuggers](https://github.com/ocornut/imgui/tree/master/misc/debuggers) to improve your debugging experience. Visual Studio users can add `imgui.natvis` and `imgui.natstepfilter` to their project.
  - Misc: std::string users: Add `misc/cpp/imgui_stdlib.*` to easily use `InputText()` with `std::string` type.

It is recommended that you follow those steps and not attempt to build Dear ImGui as a static or shared library! It's perfectly possible to do, but if you are following a "Getting Started" guide the last thing you want to do is to create yourself more problems. Note that Dear ImGui is both small and easy to build, so adding its files directly to your project should be fine. Note that Dear ImGui is a very call-heavy API, so building as a shared library is not ideal because of increased function calling overhead.

**If your application already uses the API you pulled the backends for, things should compile and link already.**

Most users with linking problems are in fact having problems because of the underlying windowing or graphics tech they use. e.g. If you use DirectX11 you need to link with d3d11.lib, if you use SDL2 you need to obtain the library (from their website or vcpkg) and link with SDL2.lib+SDL2main.lib etc. 
If you already have an app running then by definition you shouldn't have a problem including corresponding header files and linking libraries.

If you are creating a new application from scratch: while it is generally outside of scope of Dear ImGui to document how to use every windowing/graphics stacks, you can refer to our [examples/](https://github.com/ocornut/imgui/tree/master/examples) folder to see which libs/settings we are using. Some people just copy our example to start a new testbed app. For the convenience of providing easy-to-compile examples, for years our repository has included an (old) precompiled version of GLFW 3.2 for Windows.

## Setting up Dear ImGui & Backends

This list may be a little abstract. You can may skip to a dedicated "Example: If you are using XXX" section for concrete code.

- (1) Include header files for main lib (`#include "imgui.h"`) + backends (e.g. `#include "imgui_impl_win32.h"`, `#include "imgui_impl_dx11.h"`).
- (2) Create Dear ImGui context with `ImGui::CreateContext()`.
- (3) Optionally set configuration flags, load fonts, setup style.
- (4) Initialize Platform and Rendering backends (e.g. `ImGui_ImplWin32_Init()` + `ImGui_ImplDX11_Init()`).
- (5) Start of main loop: poll events + call backends' `ImGui_ImplXXX_NewFrame()` functions + call `ImGui::NewFrame()`.
- (6) End of main loop: call `ImGui::Render()` + call Render function of Rendering backend (e.g. `ImGui_ImplDX11_Render()`).
- (7) Most backends require some extra steps to hook or forward events. (e.g. calling `ImGui_ImplWin32_WndProcHandler`)
- (8) Call backend shutdown functions and destroy Dear ImGui context with `ImGui::DestroyContext()`.
- (9) In your application's input logic: you can poll `ImGui::GetIO().WantCaptureMouse`/`WantCaptureKeyboard` to check if Dear ImGui wants to obstruct mouse/keyboard inputs from underlying apps. e.g. when hovering a window `WantCaptureMouse` will be set to true, one possible strategy would be to stop passing mouse events to your main application.

## Example: If you are using Raw Win32 API + DirectX11

Full standalone example: [example_win32_directx11/main.cpp](https://github.com/ocornut/imgui/blob/master/examples/example_win32_directx11/main.cpp)

Add to Includes:
```cpp
#include "imgui.h"
#include "imgui_impl_win32.h"
#include "imgui_impl_dx11.h"
```
Add to Initialization:
```cpp
// Setup Dear ImGui context
IMGUI_CHECKVERSION();
ImGui::CreateContext();
ImGuiIO& io = ImGui::GetIO();
io.ConfigFlags |= ImGuiConfigFlags_NavEnableKeyboard;     // Enable Keyboard Controls
io.ConfigFlags |= ImGuiConfigFlags_NavEnableGamepad;      // Enable Gamepad Controls
io.ConfigFlags |= ImGuiConfigFlags_DockingEnable;         // IF using Docking Branch

// Setup Platform/Renderer backends
ImGui_ImplWin32_Init(YOUR_HWND);
ImGui_ImplDX11_Init(YOUR_D3D_DEVICE, YOUR_D3D_DEVICE_CONTEXT);
```
Add to start of main loop:
```cpp
// (Your code process and dispatch Win32 messages)
// Start the Dear ImGui frame
ImGui_ImplDX11_NewFrame();
ImGui_ImplWin32_NewFrame();
ImGui::NewFrame();
ImGui::ShowDemoWindow(); // Show demo window! :)
```
Add to end of main loop:
```cpp
// Rendering
// (Your code clears your framebuffer, renders your other stuff etc.)
ImGui::Render();
ImGui_ImplDX11_RenderDrawData(ImGui::GetDrawData());
// (Your code calls swapchain's Present() function)
```
Add to your WndProc handler:
```cpp
extern IMGUI_IMPL_API LRESULT ImGui_ImplWin32_WndProcHandler(HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam);
if (ImGui_ImplWin32_WndProcHandler(hWnd, msg, wParam, lParam))
    return true;
// (Your code process Win32 messages)
// (You should discard mouse/keyboard messages in your game/engine when io.WantCaptureMouse/io.WantCaptureKeyboard are set.)
```
Add to Shutdown:
```cpp
ImGui_ImplDX11_Shutdown();
ImGui_ImplWin32_Shutdown();
ImGui::DestroyContext();
```
That should be all!

## Example: If you are using Raw Win32 API + DirectX12

Full standalone example: [example_win32_directx12/main.cpp](https://github.com/ocornut/imgui/blob/master/examples/example_win32_directx12/main.cpp)

Add to Includes:
```cpp
#include "imgui.h"
#include "imgui_impl_win32.h"
#include "imgui_impl_dx12.h"
```
Add to Initialization:
```cpp
// Setup Dear ImGui context
IMGUI_CHECKVERSION();
ImGui::CreateContext();
ImGuiIO& io = ImGui::GetIO();
io.ConfigFlags |= ImGuiConfigFlags_NavEnableKeyboard;     // Enable Keyboard Controls
io.ConfigFlags |= ImGuiConfigFlags_NavEnableGamepad;      // Enable Gamepad Controls
io.ConfigFlags |= ImGuiConfigFlags_DockingEnable;         // IF using Docking Branch

// Setup Platform/Renderer backends
ImGui_ImplDX12_InitInfo init_info = {};
init_info.Device = YOUR_D3D_DEVICE;
init_info.CommandQueue = YOUR_COMMAND_QUEUE;
init_info.NumFramesInFlight = NUM_FRAMES_IN_FLIGHT;
init_info.RTVFormat = DXGI_FORMAT_R8G8B8A8_UNORM; // Or your render target format.

// Allocating SRV descriptors (for textures) is up to the application, so we provide callbacks.
// The example_win32_directx12/main.cpp application include a simple free-list based allocator.
init_info.SrvDescriptorHeap = YOUR_SRV_DESC_HEAP;
init_info.SrvDescriptorAllocFn = [](ImGui_ImplDX12_InitInfo*, D3D12_CPU_DESCRIPTOR_HANDLE* out_cpu_handle, D3D12_GPU_DESCRIPTOR_HANDLE* out_gpu_handle) { return YOUR_ALLOCATOR_FUNCTION_FOR_SRV_DESCRIPTORS(...); };
init_info.SrvDescriptorFreeFn = [](ImGui_ImplDX12_InitInfo*, D3D12_CPU_DESCRIPTOR_HANDLE cpu_handle, D3D12_GPU_DESCRIPTOR_HANDLE gpu_handle)            { return YOUR_FREE_FUNCTION_FOR_SRV_DESCRIPTORS(...); };

// (before 1.91.6 the DirectX12 backend required a single SRV descriptor passed)
// (there is a legacy version of ImGui_ImplDX12_Init() that supports those, but a future version of Dear ImGuii will requires more descriptors to be allocated)

```
Add to start of main loop:
```cpp
// (Your code process and dispatch Win32 messages)
// Start the Dear ImGui frame
ImGui_ImplDX12_NewFrame();
ImGui_ImplWin32_NewFrame();
ImGui::NewFrame();
ImGui::ShowDemoWindow(); // Show demo window! :)
```
Add to end of main loop:
```cpp
// Rendering
// (Your code clears your framebuffer, renders your other stuff etc.)
ImGui::Render();
ImGui_ImplDX12_RenderDrawData(ImGui::GetDrawData(), YOUR_DX12_COMMAND_LIST);
// (Your code calls ExecuteCommandLists, swapchain's Present(), etc.)
```
Add to your WndProc handler:
```cpp
extern IMGUI_IMPL_API LRESULT ImGui_ImplWin32_WndProcHandler(HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam);
if (ImGui_ImplWin32_WndProcHandler(hWnd, msg, wParam, lParam))
    return true;
(Your code process Windows messages.)
// (You should discard mouse/keyboard messages in your game/engine when io.WantCaptureMouse/io.WantCaptureKeyboard are set.)
```
Add to Shutdown:
```cpp
ImGui_ImplDX12_Shutdown();
ImGui_ImplWin32_Shutdown();
ImGui::DestroyContext();
```
That should be all!

## Example: If you are using GLFW + OpenGL/WebGL

Full standalone example: [example_glfw_opengl3/main.cpp](https://github.com/ocornut/imgui/blob/master/examples/example_glfw_opengl3/main.cpp)

Add to Includes:
```cpp
#include "imgui.h"
#include "imgui_impl_glfw.h"
#include "imgui_impl_opengl3.h"
```
Add to Initialization:
```cpp
// Setup Dear ImGui context
IMGUI_CHECKVERSION();
ImGui::CreateContext();
ImGuiIO& io = ImGui::GetIO();
io.ConfigFlags |= ImGuiConfigFlags_NavEnableKeyboard;     // Enable Keyboard Controls
io.ConfigFlags |= ImGuiConfigFlags_NavEnableGamepad;      // Enable Gamepad Controls
io.ConfigFlags |= ImGuiConfigFlags_DockingEnable;         // IF using Docking Branch

// Setup Platform/Renderer backends
ImGui_ImplGlfw_InitForOpenGL(YOUR_WINDOW, true);          // Second param install_callback=true will install GLFW callbacks and chain to existing ones.
ImGui_ImplOpenGL3_Init();
```
Add to start of main loop:
```cpp
// (Your code calls glfwPollEvents())
// ...
// Start the Dear ImGui frame
ImGui_ImplOpenGL3_NewFrame();
ImGui_ImplGlfw_NewFrame();
ImGui::NewFrame();
ImGui::ShowDemoWindow(); // Show demo window! :)
```
Add to end of main loop:
```cpp
// Rendering
// (Your code clears your framebuffer, renders your other stuff etc.)
ImGui::Render();
ImGui_ImplOpenGL3_RenderDrawData(ImGui::GetDrawData());
// (Your code calls glfwSwapBuffers() etc.)
```
Add to Shutdown:
```cpp
ImGui_ImplOpenGL3_Shutdown();
ImGui_ImplGlfw_Shutdown();
ImGui::DestroyContext();
```
Event handling:
- You should discard mouse/keyboard messages in your game/engine when io.WantCaptureMouse/io.WantCaptureKeyboard are set.

That should be all!

## Example: If you are using GLFW + Metal (on Apple devices)

Full standalone example: [example_glfw_metal/main.mm](https://github.com/ocornut/imgui/blob/master/examples/example_glfw_metal/main.mm)

```sh
brew install glfw
```

Add to Includes:
```cpp
#include "imgui.h"
#include "imgui_impl_glfw.h"
#include "imgui_impl_metal.h"
```
Add to Initialization:
```cpp
// Setup Dear ImGui context
IMGUI_CHECKVERSION();
ImGui::CreateContext();
ImGuiIO& io = ImGui::GetIO();
io.ConfigFlags |= ImGuiConfigFlags_NavEnableKeyboard;     // Enable Keyboard Controls
io.ConfigFlags |= ImGuiConfigFlags_NavEnableGamepad;      // Enable Gamepad Controls
io.ConfigFlags |= ImGuiConfigFlags_DockingEnable;         // IF using Docking Branch

// Setup Platform/Renderer backends
ImGui_ImplGlfw_InitForOpenGL(YOUR_WINDOW, true);          // Second param install_callback=true will install GLFW callbacks and chain to existing ones.
ImGui_ImplMetal_Init(YOUR_METAL_DEVICE);
```
Add to start of main loop:
```cpp
// (Your code calls glfwPollEvents())
// ...
// Start the Dear ImGui frame
ImGui_ImplMetal_NewFrame(YOUR_RENDER_PASS_DESCRIPTOR);
ImGui_ImplGlfw_NewFrame();
ImGui::NewFrame();
ImGui::ShowDemoWindow(); // Show demo window! :)
```
Add to end of main loop:
```cpp
// Rendering
// (Your code clears your framebuffer, renders your other stuff etc.)
ImGui::Render();
ImGui_ImplMetal_RenderDrawData(ImGui::GetDrawData(), YOUR_METAL_COMMAND_BUFFER, YOUR_METAL_RENDER_ENCODER);
// (Your code calls endEncoding, presentDrawable, commit etc.)
```
Add to Shutdown:
```cpp
ImGui_ImplMetal_Shutdown();
ImGui_ImplGlfw_Shutdown();
ImGui::DestroyContext();
```
Event handling:
- You should discard mouse/keyboard messages in your game/engine when io.WantCaptureMouse/io.WantCaptureKeyboard are set.

That should be all!

## Example: If you are using SDL2/SDL3 + OpenGL/WebGL

Full standalone example for SDL2: [example_sdl2_opengl3/main.cpp](https://github.com/ocornut/imgui/blob/master/examples/example_sdl2_opengl3/main.cpp)
<BR>Full standalone example for SDL3: [example_sdl3_opengl3/main.cpp](https://github.com/ocornut/imgui/blob/master/examples/example_sdl3_opengl3/main.cpp)

All instructions below are for SDL2. Simply replace "SDL2" with "SDL3" to get SDL3 equivalent.

Add to Includes:
```cpp
#include "imgui.h"
#include "imgui_impl_sdl2.h"
#include "imgui_impl_opengl3.h"
```
Add to Initialization:
```cpp
// Setup Dear ImGui context
IMGUI_CHECKVERSION();
ImGui::CreateContext();
ImGuiIO& io = ImGui::GetIO();
io.ConfigFlags |= ImGuiConfigFlags_NavEnableKeyboard;     // Enable Keyboard Controls
io.ConfigFlags |= ImGuiConfigFlags_NavEnableGamepad;      // Enable Gamepad Controls
io.ConfigFlags |= ImGuiConfigFlags_DockingEnable;         // IF using Docking Branch

// Setup Platform/Renderer backends
ImGui_ImplSDL2_InitForOpenGL(window, YOUR_SDL_GL_CONTEXT);
ImGui_ImplOpenGL3_Init();
```
Add to start of main loop:
```cpp
// (Where your code calls SDL_PollEvent())
ImGui_ImplSDL2_ProcessEvent(&event); // Forward your event to backend
// (You should discard mouse/keyboard messages in your game/engine when io.WantCaptureMouse/io.WantCaptureKeyboard are set.)
```
```cpp
// (After event loop)
// Start the Dear ImGui frame
ImGui_ImplOpenGL3_NewFrame();
ImGui_ImplSDL2_NewFrame();
ImGui::NewFrame();
ImGui::ShowDemoWindow(); // Show demo window! :)
```
Add to end of main loop:
```cpp
// Rendering
// (Your code clears your framebuffer, renders your other stuff etc.)
ImGui::Render();
ImGui_ImplOpenGL3_RenderDrawData(ImGui::GetDrawData());
// (Your code calls SDL_GL_SwapWindow() etc.)
```
Add to Shutdown:
```cpp
ImGui_ImplOpenGL3_Shutdown();
ImGui_ImplSDL2_Shutdown();
ImGui::DestroyContext();
```

That should be all!

## Example: If you are using SDL2/SDL3 + Vulkan

Full standalone example for SDL2+Vulkan: [example_sdl2_vulkan/main.cpp](https://github.com/ocornut/imgui/blob/master/examples/example_sdl2_vulkan/main.cpp)
<BR>Full standalone example for SDL3+Vulkan: [example_sdl3_vulkan/main.cpp](https://github.com/ocornut/imgui/blob/master/examples/example_sdl3_vulkan/main.cpp)
<BR>Full standalone example for GLFW+Vulkan: [example_glfw_vulkan/main.cpp](https://github.com/ocornut/imgui/blob/master/examples/example_glfw_vulkan/main.cpp)

Unfortunately this is the most complex one and may not work with all app setups. We are always working on making imgui_impl_vulkan.cpp more compatible with existing engines, so please don't hesitate to post feedback.

You must provide a Descriptor Pool with room for at least `IMGUI_IMPL_VULKAN_MINIMUM_IMAGE_SAMPLER_POOL_SIZE` combined image sampler (`VK_DESCRIPTOR_TYPE_COMBINED_IMAGE_SAMPLER`). You may also set the ImGui_ImplVulkan_InitInfo::DescriptorPoolSize field to that or a larger value for the backend to automatically create one for you, which won't be shared with your app.

All instructions below are for SDL3. Simply replace "SDL2" with "SDL3" to get SDL3 equivalent.

Add to Includes:
```cpp
#include "imgui.h"
#include "imgui_impl_sdl2.h"
#include "imgui_impl_vulkan.h"

static void check_vk_result(VkResult err)
{
    if (err == 0)
        return;
    fprintf(stderr, "[vulkan] Error: VkResult = %d\n", err);
    if (err < 0)
        abort();
}
```
Add to Initialization:
```cpp
// Setup Dear ImGui context
IMGUI_CHECKVERSION();
ImGui::CreateContext();
ImGuiIO& io = ImGui::GetIO();
io.ConfigFlags |= ImGuiConfigFlags_NavEnableKeyboard;     // Enable Keyboard Controls
io.ConfigFlags |= ImGuiConfigFlags_NavEnableGamepad;      // Enable Gamepad Controls
io.ConfigFlags |= ImGuiConfigFlags_DockingEnable;         // IF using Docking Branch

// Setup Platform/Renderer backends
ImGui_ImplSDL2_InitForVulkan(YOUR_SDL_WINDOW);
ImGui_ImplVulkan_InitInfo init_info = {};
init_info.Instance = YOUR_INSTANCE;
init_info.PhysicalDevice = YOUR_PHYSICAL_DEVICE;
init_info.Device = YOUR_DEVICE;
init_info.QueueFamily = YOUR_QUEUE_FAMILY;
init_info.Queue = YOUR_QUEUE;
init_info.PipelineCache = YOUR_PIPELINE_CACHE;
init_info.DescriptorPool = YOUR_DESCRIPTOR_POOL;
init_info.MinImageCount = 2;
init_info.ImageCount = 2;
init_info.Allocator = YOUR_ALLOCATOR;
init_info.PipelineInfoMain.RenderPass = wd->RenderPass;
init_info.PipelineInfoMain.Subpass = 0;
init_info.PipelineInfoMain.MSAASamples = VK_SAMPLE_COUNT_1_BIT;
init_info.CheckVkResultFn = check_vk_result;
ImGui_ImplVulkan_Init(&init_info);
```
Add to start of main loop:
```cpp
// (Where your code calls SDL_PollEvent())
ImGui_ImplSDL2_ProcessEvent(&event); // Forward your event to backend
// (You should discard mouse/keyboard messages in your game/engine when io.WantCaptureMouse/io.WantCaptureKeyboard are set.)

```
```cpp
// (After event loop)
// Start the Dear ImGui frame
ImGui_ImplVulkan_NewFrame();
ImGui_ImplSDL2_NewFrame();
ImGui::NewFrame();
ImGui::ShowDemoWindow(); // Show demo window! :)
```
Add to end of main loop:
```cpp
// Rendering
// (Your code clears your framebuffer, renders your other stuff etc.)
ImGui::Render();
ImGui_ImplVulkan_RenderDrawData(ImGui::GetDrawData(), YOUR_COMMAND_BUFFER);
// (Your code calls vkCmdEndRenderPass, vkQueueSubmit, vkQueuePresentKHR etc.)
```
Add to Shutdown:
```cpp
ImGui_ImplVulkan_Shutdown();
ImGui_ImplSDL2_Shutdown();
ImGui::DestroyContext();
```

That should be all!

## Example: If you are using SDL3 + SDL_GPU

Full standalone example [example_sdl3_sdlgpu3/main.cpp](https://github.com/ocornut/imgui/blob/master/examples/example_sdl3_sdlgpu3/main.cpp)

Add to Includes:
```cpp
#include "imgui.h"
#include "imgui_impl_sdl3.h"
#include "imgui_impl_sdlgpu3.h"
```
Add to Initialization:
```cpp
// Setup Dear ImGui context
IMGUI_CHECKVERSION();
ImGui::CreateContext();
ImGuiIO& io = ImGui::GetIO();
io.ConfigFlags |= ImGuiConfigFlags_NavEnableKeyboard;     // Enable Keyboard Controls
io.ConfigFlags |= ImGuiConfigFlags_NavEnableGamepad;      // Enable Gamepad Controls
io.ConfigFlags |= ImGuiConfigFlags_DockingEnable;         // IF using Docking Branch

// Setup Platform/Renderer backends
ImGui_ImplSDL3_InitForSDLGPU(window);
ImGui_ImplSDLGPU3_InitInfo init_info = {};
init_info.Device = gpu_device;
init_info.ColorTargetFormat = SDL_GetGPUSwapchainTextureFormat(gpu_device, window);
init_info.MSAASamples = SDL_GPU_SAMPLECOUNT_1;                      // Only used in multi-viewports mode.
init_info.SwapchainComposition = SDL_GPU_SWAPCHAINCOMPOSITION_SDR;  // Only used in multi-viewports mode.
init_info.PresentMode = SDL_GPU_PRESENTMODE_VSYNC;
ImGui_ImplSDLGPU3_Init(&init_info);
```
Add to start of main loop:
```cpp
// (Where your code calls SDL_PollEvent())
ImGui_ImplSDL3_ProcessEvent(&event); // Forward your event to backend
// (You should discard mouse/keyboard messages in your game/engine when io.WantCaptureMouse/io.WantCaptureKeyboard are set.)
```
```cpp
// (After event loop)
// Start the Dear ImGui frame
ImGui_ImplSDLGPU3_NewFrame();
ImGui_ImplSDL3_NewFrame();
ImGui::NewFrame();
ImGui::ShowDemoWindow(); // Show demo window! :)
```
Add to end of main loop:
```cpp
// Rendering
// (Your code clears your framebuffer, renders your other stuff etc.)
ImGui::Render();

SDL_GPUCommandBuffer* command_buffer = SDL_AcquireGPUCommandBuffer(gpu_device); // Acquire a GPU command buffer
SDL_WaitAndAcquireGPUSwapchainTexture(command_buffer, window, &swapchain_texture, nullptr, nullptr); // Acquire a swapchain texture

ImGui_ImplSDLGPU3_PrepareDrawData(draw_data, command_buffer);

// Setup and start a render pass
SDL_GPUColorTargetInfo target_info = {};
target_info.texture = swapchain_texture;
target_info.clear_color = SDL_FColor { clear_color.x, clear_color.y, clear_color.z, clear_color.w };
target_info.load_op = SDL_GPU_LOADOP_CLEAR;
target_info.store_op = SDL_GPU_STOREOP_STORE;
target_info.mip_level = 0;
target_info.layer_or_depth_plane = 0;
target_info.cycle = false;
SDL_GPURenderPass* render_pass = SDL_BeginGPURenderPass(command_buffer, &target_info, 1, nullptr);

// Render ImGui
ImGui_ImplSDLGPU3_RenderDrawData(draw_data, command_buffer, render_pass);

SDL_EndGPURenderPass(render_pass);
```
Add to Shutdown:
```cpp
ImGui_ImplSDL3_Shutdown();
ImGui_ImplSDLGPU3_Shutdown();
ImGui::DestroyContext();
```
That should be all!

## Using another combination of backends?

The various examples above should reflect integration with a majority of backends, so you can follow the same logic.
Some backends require more information from you (e.g. in particular Vulkan and DirectX12 rendering backends). When in doubt, refer to the corresponding [examples](https://github.com/ocornut/imgui/tree/master/examples) application.

## Additional code to enable Docking

To use the [Docking](https://github.com/ocornut/imgui/wiki/Docking) feature, pull the `docking` branch and enable the configuration flag:
```cpp
io.ConfigFlags |= ImGuiConfigFlags_DockingEnable; 
```
## Additional code to enable Multi-viewports

To use the [Multi-viewports](https://github.com/ocornut/imgui/wiki/Multi-Viewports) feature, pull the `docking` branch and enable the configuration flag:
```cpp
io.ConfigFlags |= ImGuiConfigFlags_ViewportsEnable; 
```
At the end of your render loop, generally after rendering your main viewport but before presenting/swapping it:
```cpp
if (io.ConfigFlags & ImGuiConfigFlags_ViewportsEnable)
{
    // Update and Render additional Platform Windows
    ImGui::UpdatePlatformWindows();
    ImGui::RenderPlatformWindowsDefault();

    // TODO for OpenGL: restore current GL context.
}
```

Note that there may be additional calls required surrounding this depending on the backend you are using (**OpenGL in particular needs backup/restore of current GL context**). Check the [example project](https://github.com/ocornut/imgui/tree/docking/examples) appropriate to your setup for details.

## Once you are setup...

- Run `ImGui::ShowDemoWindow()`. Browse imgui_demo.cpp to find how things are done. 
- You may also refer to @pthom's [imgui_explorer](https://pthom.github.io/imgui_explorer) which matches the output of the demo window with corresponding source code.
- Use [Item Picker](https://github.com/ocornut/imgui/wiki/Debug-Tools) to easily debug break into the code of a given item.
- Read [Wiki](https://github.com/ocornut/imgui/wiki) for more.
- You may edit `imconfig.h` or use `#define IMGUI_USER_CONFIG \"my_imconfig.h\"` to use compile-time configuration features.
