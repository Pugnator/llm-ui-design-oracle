<!-- source: https://github.com/ocornut/imgui/wiki/Multi-Viewports
     fetched: 2026-09-19
     licence: MIT — https://github.com/ocornut/imgui/blob/master/LICENSE.txt
     title: Dear ImGui wiki — Multi-Viewports
     version: Dear ImGui 1.93.0 WIP (master, 2026-09-19) -->

- Development Thread: https://github.com/ocornut/imgui/issues/1542
- Open Issues: https://github.com/ocornut/imgui/labels/multi-viewports
- Also see: [Glossary: Multi-Viewports terms](Glossary#multi-viewports-terms).

![MultiViewports](https://user-images.githubusercontent.com/8225057/97542423-fe8ffb80-19c6-11eb-9bf5-e26d86364e55.png)

#### What is it?

Multi-viewports is the feature allowing you to **seamlessly extract Dear ImGui windows out of your main rendering context**. In traditional game programming, your engine/game generally create an OS window associated to a graphics context (e.g. using DirectX, OpenGL) and all rendering has to happen inside this graphics context. 

With multi-viewports, Dear ImGui gets the ability to create new OS windows and graphics contexts, as required to host Dear ImGui that have been moved outside the boundaries of the primary OS window. This is achieved via a set of flags and functions (inside `ImGuiPlatformIO` structure) which allows Dear ImGui to communicate with individual back-ends. **Most back-ends provided in the `backends/` folder can support multi-viewports**.

Among other things, Multi-viewports also facilitate the use of Dear ImGui over multiple monitors. 

#### Where to find it?

Multi-viewports are currently available in the [docking](https://github.com/ocornut/imgui/tree/docking) branch. This is a well maintained branch and most large teams have been using this branch for a while. It is safe and recommended to use that branch.

#### How can I enable Multi-viewports ?

If you are using platform and renderer back-ends from the `backends/` folder, they already support multi-viewports.

- Add to your configuration flags:

```cpp
io.ConfigFlags |= ImGuiConfigFlags_ViewportsEnable;
```

- Add in your main loop, after rendering your main viewport:
```cpp
// Update and Render additional Platform Windows
if (io.ConfigFlags & ImGuiConfigFlags_ViewportsEnable)
{
    ImGui::UpdatePlatformWindows();
    ImGui::RenderPlatformWindowsDefault();
    // TODO for OpenGL: restore current GL context.
}
```

That's pretty much it.
There may be additional calls required surrounding this depending on the backend you are using: OpenGL in particular needs backup/restore of current GL context. Check the [example project](https://github.com/ocornut/imgui/tree/docking/examples) appropriate to your setup for details.

There are a few additional multi-viewports related configuration flags in the IO structure which you may toy with.

If you are using a custom back-end, refer to the `ImGuiPlatformIO` structure and existing `backends/` + `examples/` to implement support for multi-viewports in your engine. This is not particularly easy to add. 

#### Issues

- The feature tends to be broken on Linux/X11 with many window managers. It's been endlessly reported and will only likely ever be fixed if a Linux user wants to commit the time to investigate this seriously (aka run and implement new tests, and test their changes on other OS than their own). See [#2117](https://github.com/ocornut/imgui/issues/2117).
- The feature doesn't work in Wayland. Wayland doesn't let application read or write windows positions.

#### FAQ

- Q: What happens to the coordinate systems?
- A: When enabling `ImGuiConfigFlags_ViewportsEnable`, the coordinate system used by Dear ImGui changes to match the coordinate system of your OS/desktop (e.g. (0,0) generally becomes the top-left corner of your primary monitor). This shouldn't affect most code, but if you have code using absolute coordinates you may want to change them to be relative to a window, relative to a monitor or relative to your main viewport (`GetMainViewport()->Pos`).

- Q: How to handle varying DPI over multiple monitors?
- A: See [this FAQ entry](https://github.com/ocornut/imgui/blob/master/docs/FAQ.md#q-how-should-i-handle-dpi-in-my-application).
